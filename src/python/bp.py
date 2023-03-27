from grongier.pex import BusinessProcess

from msg import FhirRequest,OrganizationRequest

from fhir.resources.organization import Organization
from fhir.resources.address import Address
from fhir.resources.contactpoint import ContactPoint


class ProcessCSV(BusinessProcess):

    def on_request(self, request):
        """
        If the bp receives an OrgaRequest,iIt creates a new Organization object, 
        fills it with the information from the request and sends it to the FhirClient

        If the request is a FhirRequest, it sends it to the FhirClient.
        
        :param request: The request object that was sent to the service
        :return: None
        """
        if isinstance(request, OrganizationRequest):
            # Creates a new Organization and fill it with the information from request
            # This is the DataTransformation step

            # Get the resource from the request
            base_orga = request.resource

            # Creation of the object FHIR Organization
            organization = Organization()

            # Mapping of the information from the request to the Organization object
            organization.name = base_orga.name

            organization.active = base_orga.active

            # Creation of the Address object and mapping of the information 
            # from the request to the Address object
            adress = Address()
            adress.country = base_orga.country
            adress.city = base_orga.city

            # Setting the adress of our organization to the one we created
            organization.address = [adress]

            # Creation of the ContactPoint object and mapping of the
            # information from the request to the ContactPoint object
            telecom = ContactPoint()
            telecom.value = base_orga.value
            telecom.system = base_orga.system
            # Setting the telecom of our organization to the one we created
            organization.telecom = [telecom]

            # Now, our DT is done, we have an object organization that is a 
            # FHIR R4 object and holds all of our csv information.
            # Now we can send the Organization to the FhirClient by using a request
            msg = FhirRequest()
            msg.resource = organization

            self.send_request_sync("Python.bo.FhirClient", msg)
        
        if isinstance(request,FhirRequest):
            self.send_request_sync("Python.bo.FhirClient", request)       

        return None
