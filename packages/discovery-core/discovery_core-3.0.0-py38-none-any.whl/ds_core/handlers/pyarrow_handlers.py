import ast
import os
import pyarrow as pa
import pyarrow.parquet as pq
import pyarrow.feather as feather
from ds_core.components.core_commons import CoreCommons
from pyarrow import csv

from ds_core.handlers.abstract_handlers import AbstractSourceHandler, AbstractPersistHandler
from ds_core.handlers.abstract_handlers import ConnectorContract, HandlerFactory

__author__ = 'Darryl Oatridge'


class PyarrowSourceHandler(AbstractSourceHandler):
    """ PyArrow read only Source Handler. """

    def __init__(self, connector_contract: ConnectorContract):
        """ initialise the Handler passing the connector_contract dictionary """
        super().__init__(connector_contract)
        self._file_state = 0
        self._changed_flag = True

    def supported_types(self) -> list:
        """ The source types supported with this module"""
        return ['parquet', 'feather', 'csv', 'json', 'xml', 'pickle', 'xlsx']

    def load_canonical(self, **kwargs) -> pa.Table:
        """ returns the canonical dataset based on the connector contract. """
        if not isinstance(self.connector_contract, ConnectorContract):
            raise ValueError("The Connector Contract was not been set at initialisation or is corrupted")
        _cc = self.connector_contract
        load_params = kwargs
        load_params.update(_cc.kwargs)  # Update with any kwargs in the Connector Contract
        if load_params.pop('use_full_uri', False):
            file_type = load_params.pop('file_type', 'csv')
            address = _cc.uri
        else:
            load_params.update(_cc.query)  # Update kwargs with those in the uri query
            _, _, _ext = _cc.address.rpartition('.')
            address = _cc.address
            file_type = load_params.pop('file_type', _ext if len(_ext) > 0 else 'csv')
        self.reset_changed()
        # parquet
        if file_type.lower() in ['parquet', 'pqt', 'pq']:
            return pq.read_table(address, **load_params)
        # feathers
        if file_type.lower() in ['feather']:
            return feather.read_table(address, **load_params)
        # csv
        if file_type.lower() in ['csv', 'gz', 'bz2']:
            parse_options = csv.ParseOptions(**load_params)
            return csv.read_csv(address, parse_options=parse_options)
        # json and complex nested
        if file_type.lower() in ['complex', 'nested', 'txt', 'json']:
            with open(address) as f:
                document = f.read()
            for i in ['\n', '\t', ' ']:
                document = document.replace(i, '')
            document = document.replace('null', 'None').replace('true', 'True').replace('false', 'False')
            document = pa.Table.from_pylist(list(eval(document)))
            return CoreCommons.table_flatten(document)
        raise LookupError('The source format {} is not currently supported'.format(file_type))

    def exists(self) -> bool:
        """ Returns True is the file exists """
        if not isinstance(self.connector_contract, ConnectorContract):
            raise ValueError("The Pandas Connector Contract has not been set")
        _cc = self.connector_contract
        if _cc.schema.startswith('http') or _cc.schema.startswith('git'):
            module_name = 'requests'
            _address = _cc.address.replace("git://", "https://")
            if HandlerFactory.check_module(module_name=module_name):
                module = HandlerFactory.get_module(module_name=module_name)
                return module.get(_address).status_code == 200
            raise ModuleNotFoundError(f"The required module {module_name} has not been installed. "
                                      f"Please pip install the appropriate package in order to complete this action")
        if os.path.exists(_cc.address):
            return True
        return False

    def has_changed(self) -> bool:
        """ returns the status of the change_flag indicating if the file has changed since last load or reset"""
        if not self.exists():
            return False
        # maintain the change flag
        _cc = self.connector_contract
        if _cc.schema.startswith('http') or _cc.schema.startswith('git'):
            if not isinstance(self.connector_contract, ConnectorContract):
                raise ValueError("The Pandas Connector Contract has not been set")
            module_name = 'requests'
            _address = _cc.address.replace("git://", "https://")
            if HandlerFactory.check_module(module_name=module_name):
                module = HandlerFactory.get_module(module_name=module_name)
                state = module.head(_address).headers.get('last-modified', 0)
            else:
                raise ModuleNotFoundError(f"The required module {module_name} has not been installed. Please pip "
                                          f"install the appropriate package in order to complete this action")
        else:
            state = os.stat(_cc.address).st_mtime_ns
        if state != self._file_state:
            self._changed_flag = True
            self._file_state = state
        return self._changed_flag

    def reset_changed(self, changed: bool = False):
        """ manual reset to say the file has been seen. This is automatically called if the file is loaded"""
        changed = changed if isinstance(changed, bool) else False
        self._changed_flag = changed


class PyarrowPersistHandler(PyarrowSourceHandler, AbstractPersistHandler):
    """ PyArrow read/write Persist Handler. """

    def persist_canonical(self, canonical: pa.Table, **kwargs) -> bool:
        """ persists the canonical dataset

        Extra Parameters in the ConnectorContract kwargs:
            - file_type: (optional) the type of the source file. if not set, inferred from the file extension
        """
        if not isinstance(self.connector_contract, ConnectorContract):
            return False
        _uri = self.connector_contract.uri
        return self.backup_canonical(uri=_uri, canonical=canonical, **kwargs)

    def backup_canonical(self, canonical: pa.Table, uri: str, **kwargs) -> bool:
        """ creates a backup of the canonical to an alternative URI

        Extra Parameters in the ConnectorContract kwargs:
            - file_type: (optional) the type of the source file. if not set, inferred from the file extension
            - write_params (optional) a dictionary of additional write parameters directly passed to 'write_' methods
        """
        if not isinstance(self.connector_contract, ConnectorContract):
            return False
        _cc = self.connector_contract
        _address = _cc.parse_address(uri=uri)
        persist_params = kwargs if isinstance(kwargs, dict) else _cc.kwargs
        persist_params.update(_cc.parse_query(uri=uri))
        _, _, _ext = _address.rpartition('.')
        if not self.connector_contract.schema.startswith('http'):
            _path, _ = os.path.split(_address)
            if len(_path) > 0 and not os.path.exists(_path):
                os.makedirs(_path)
        file_type = persist_params.pop('file_type', _ext if len(_ext) > 0 else 'parquet')
        write_params = persist_params.pop('write_params', {})
        # parquet
        if file_type.lower() in ['pq', 'pqt', 'parquet']:
            pq.write_table(canonical, _address, **write_params)
            return True
        # feather
        if file_type.lower() in ['feather']:
            feather.write_feather(canonical, _address, **write_params)
            return True
        # csv
        if file_type.lower() in ['csv', 'gz', 'bz2']:
            csv.write_csv(canonical, _address, **write_params)
            return True
        # json and complex nested
        if file_type.lower() in ['complex', 'nested', 'txt', 'json']:
            values = CoreCommons.table_nest(canonical)
            with open(_address, 'w') as f:
                f.write(str(values))
            return True
        # not found
        raise LookupError('The file format {} is not currently supported for write'.format(file_type))

    def remove_canonical(self) -> bool:
        if not isinstance(self.connector_contract, ConnectorContract):
            return False
        _cc = self.connector_contract
        if self.connector_contract.schema.startswith('http'):
            raise NotImplemented("Remove Canonical does not support {} schema based URIs".format(_cc.schema))
        if os.path.exists(_cc.address):
            os.remove(_cc.address)
            return True
        return False
