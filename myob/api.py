from .credentials import PartnerCredentials
from .endpoints import ALL, ENDPOINTS, GET
from .managers import Manager
from .constants import MYOB_BASE_URL

class Myob:
    """ An ORM-like interface to the MYOB API. """
    def __init__(self, credentials, base_url=None):
        if not base_url:
            base_url = MYOB_BASE_URL
        if not isinstance(credentials, PartnerCredentials):
            raise TypeError(
                'Expected a Credentials instance, got %s.' % (
                    type(credentials).__name__,
                )
            )
        self.credentials = credentials
        self.companyfiles = CompanyFiles(credentials, base_url)
        self._manager = Manager('', credentials, base_url, raw_endpoints=[
            (GET, 'Info/', 'Return API build information for each individual endpoint.'),
        ])

    def info(self):
        return self._manager.info()

    def __repr__(self):
        return 'Myob:\n    %s' % '\n    '.join(['companyfiles', 'info'])


class CompanyFiles:
    def __init__(self, credentials, base_url):
        self.base_url = base_url
        self.credentials = credentials
        self._manager = Manager('', self.credentials, base_url, raw_endpoints=[
            (ALL, '', 'Return a list of company files.'),
            (GET, '[id]/', 'List endpoints available for a company file.'),
        ])
        self._manager.name = 'CompanyFile'

    def all(self):
        raw_companyfiles = self._manager.all()
        return [CompanyFile(raw_companyfile, self.credentials, self.base_url) for raw_companyfile in raw_companyfiles]

    def get(self, id, call=True):
        if call:
            # raw_companyfile = self._manager.get(id=id)['CompanyFile']
            # NOTE: Annoyingly, we need to pass company_id to the manager, else we won't have permission
            # on the GET endpoint. The only way we currently allow passing company_id is by setting it on the manager,
            # and we can't do that on init, as this is a manager for company files plural..
            # Reluctant to change manager code, as it would add confusion if the inner method let you override the company_id.
            manager = Manager('', self.credentials, self.base_url, raw_endpoints=[(GET, '', '')], company_id=id)
            raw_companyfile = manager.get()['CompanyFile']
        else:
            raw_companyfile = {'Id': id}
        return CompanyFile(raw_companyfile, self.credentials, self.base_url)

    def __repr__(self):
        return self._manager.__repr__()


class CompanyFile:
    def __init__(self, raw, credentials, base_url):
        self.id = raw['Id']
        self.name = raw.get('Name')
        self.data = raw  # Dump remaining raw data here.
        self.credentials = credentials
        self.base_url = base_url
        for k, v in ENDPOINTS.items():
            setattr(self, v['name'], Manager(k, credentials, base_url, endpoints=v['methods'], company_id=self.id))

    def __repr__(self):
        return 'CompanyFile:\n    %s' % '\n    '.join(sorted(v['name'] for v in ENDPOINTS.values()))
