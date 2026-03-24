from .enterprise_management_exception import EnterpriseManagementException
from .enterprise_project import EnterpriseProject
from datetime import datetime
import json

"""Module """

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_achronym: str, project_description: str,
                         department: str, date: str, budget: float):
        # CIF Check
        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("Invalid Company Cif")
        if not self.validate_cif(company_cif):
            raise EnterpriseManagementException("Invalid Company Cif")

        objProject = EnterpriseProject(company_cif, project_achronym, project_description,
                                       department, date, budget)

        return objProject.project_id


    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""

        if not cif[0].isalpha():
            return False
        if not len(cif) == 9:
            return False

        return True
