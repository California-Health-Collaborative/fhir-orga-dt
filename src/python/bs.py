from grongier.pex import BusinessService

from dataclass_csv import DataclassReader

import obj
import msg

import os

class ServiceCSV(BusinessService):

    def get_adapter_type():
        """
        Name of the registred adaptor
        """
        return "Ens.InboundAdapter"

    def on_init(self):
        """
        It changes the current path to the file to the one specified in the path 
        attribute of the object, or to '/home/irisowner/fhirapp/python/csv/' if no path attribute
        is specified, it changes the filename and the fhir_type used for mapping if needed.
        :return: None
        """
        if not hasattr(self,'path'):
            #self.path = '/home/irisowner/fhirapp/src/python/csv/'
            self.path = "/irisdev/app/src/python/csv/"
        if not hasattr(self,'filename'):
            # Note that the filename is really important as everything else depends on it.
            # It must be the name of a Fhir resource having it's first letter capitalized.
            self.filename = 'Organization.csv'

        try:
            # At start, check if the file is in the right folder
            os.rename(self.path + "used/" + self.filename  , self.path + self.filename)
        except:
            pass

        return None

    def on_process_input(self,request):
        """
        It reads the `self.filename = "Name_of_file.csv"` file, creates an Name_of_fileRequest message for 
        each row following the BaseName_of_file dataclass, and sends it to the
        Python.ProcessCSV process.
        
        :param request: the request object
        :return: None
        """
        # Find the class to use to map the csv ( here "Base" + "Organization" => BaseOrganization )
        class_to_read = getattr(obj, "Base" + self.filename.split('.')[0])
        # Find the right message to send to the process (here "Organization" + "Request" => OrganizationRequest)
        msg_to_send = getattr(msg, self.filename.split('.')[0] + 'Request')
        # We open the file
        with open(self.path + self.filename,encoding="utf-8") as csv:
            # We read it and map it using the object BaseOrganization from earlier
            reader = DataclassReader(csv, class_to_read ,delimiter=";")
            # For each of those organization, we can create a request and send it to the process
            for row in reader:
                requ = msg_to_send()
                requ.resource = row
                self.send_request_sync('Python.bp.ProcessCSV',requ)

        # Once the file is read, it is moved to the used folder
        os.rename(self.path + self.filename, self.path + "used/" + self.filename)

        return None

