""" ADD SOMETHING """
import json
from datetime import datetime

from .enterprise_management_exception import EnterpriseManagementException
from .enterprise_project import EnterpriseProject

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_achronym: str, project_description: str,
                         department: str, date: str, budget: float):
        """ ADD DOCSTRING"""
        # CIF Check
        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("Invalid Company Cif")
        if not self.validate_cif(company_cif):
            raise EnterpriseManagementException("Invalid Company Cif")

        # Project_acronym Check
        if not isinstance(project_achronym, str):
            raise EnterpriseManagementException("Invalid Project Acronym")
        if not 5 <= len(project_achronym) <= 10:
            raise EnterpriseManagementException("Invalid Project Acronym")

        # isalnum() checks for a-z, A-Z, 0-9
        if not project_achronym.isalnum():
            raise EnterpriseManagementException("Invalid Project Acronym Characters")

        # Project_description check
        if not isinstance(project_description, str):
            raise EnterpriseManagementException("Invalid Project Description")
        if not 10 <= len(project_description) <= 30:
            raise EnterpriseManagementException("Invalid Project Description Length")

        # department check
        if not isinstance(department, str):
            raise EnterpriseManagementException("Invalid Department")
        if department not in ("HR", "Finance", "Legal", "Logistics"):
            raise EnterpriseManagementException("Invalid Department")

        # date check
        if not isinstance(date, str):
            raise EnterpriseManagementException("Invalid Date")
        try:
            date_valid = datetime.strptime(date, "%d/%m/%Y").date()
            year = date_valid.year

            if date_valid < datetime.today().date():
                raise ValueError
            if not 2025 <= year <= 2027:
                raise ValueError
        except ValueError as exc:
            raise EnterpriseManagementException("Invalid Date") from exc

        # budget check
        try:
            if not isinstance(budget, float):
                raise ValueError
            if not (budget * 100).is_integer():
                raise ValueError
            if not 50000.00 <= budget <= 1000000.00:
                raise ValueError
        except ValueError as exc:
            raise EnterpriseManagementException("Invalid Budget") from exc

        obj_project = EnterpriseProject(company_cif, project_achronym, project_description,
                                       department, date, budget)
        try:
            project_id = obj_project.project_id
        except Exception as exc:
            raise EnterpriseManagementException("MD5 String Error") from exc

        try:
            with open("corporate_operations.json", "w", encoding= "utf-8") as file:
                json.dump(obj_project.to_json(), file, indent=4)
        except OSError as exc:
            raise EnterpriseManagementException("Error Writing to JSON File") from exc

        return project_id


    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""

        if not cif[0].isalpha():
            return False
        if not len(cif) == 9:
            return False

        return True
