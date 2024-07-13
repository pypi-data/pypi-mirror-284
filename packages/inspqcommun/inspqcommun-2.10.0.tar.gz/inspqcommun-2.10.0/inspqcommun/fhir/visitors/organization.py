from fhirclient.models.organization import Organization, OrganizationContact
from fhirclient.models.fhirdate import FHIRDate
from fhirclient.models.period import Period
from fhirclient.models.extension import Extension
from fhirclient.models.meta import Meta
from fhirclient.models.address import Address
from fhirclient.models.reference import Reference
from fhirclient.models.identifier import Identifier
from fhirclient.models.contactpoint import ContactPoint

from inspqcommun.fhir.visitors.base import BaseVisitor

class OrganizationVisitor(BaseVisitor):
    
    RRSS_SYSTEM = 'https://pro.consultation.rrss.rtss.qc.ca'
    HORS_RRSS_SYSTEM = 'https://horsrrss.santepublique.rtss.qc.ca'
    RRSS_MOT_CLE_EXTENSION_URL = 'http://www.santepublique.rtss.qc.ca/sipmi/rrss/1.0.0/extensions/#motscles'
    PERIOD_URL = "http://www.santepublique.rtss.qc.ca/sipmi/rrss/1.0.0/extensions/period"

    def __init__(self, fhir_resource=None) -> None:
        self.setFhirResource(fhir_resource=fhir_resource if fhir_resource else Organization())

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, OrganizationVisitor):
            return False
        if self.get_id() != value.get_id():
            return False
        if self.get_name() != value.get_name():
            return False
        if self.get_id_rrss() != value.get_id_rrss():
            return False
        if self.get_id_hors_rrss() != value.get_id_hors_rrss():
            return False
        if self.get_telecoms() is not None and len(self.get_telecoms()) > 0:
            for telecom in self.get_telecoms():
                if value.get_telecoms() is None or len(value.get_telecoms()) == 0:
                    return False
                if telecom not in value.get_telecoms():
                    telcom_found = False
                    for value_telecom in value.get_telecoms():
                        if telecom.system == value_telecom.system and telecom.value == value_telecom.value and telecom.use == value_telecom.use:
                            telcom_found = True
                            break
                    if not telcom_found:
                        return False
        else:
            if value.get_telecoms() is not None and len(value.get_telecoms()) > 0:
                return False
        if self.get_address() is not None and len(self.get_address()) > 0:
            for address in self.get_address():
                address_found = False
                for value_address in value.get_address():
                    if address.city == value_address.city and address.state == value_address.state and address.postalCode == value_address.postalCode and address.country == value_address.country:
                        if address.line is None and value_address.line is not None:
                            return False
                        if value_address.line is None and address.line is not None:
                            return False    
                        for line in address.line:
                            if line not in value_address.line:
                                return False
                        address_found = True
                        break
                if not address_found:
                    return False
        else:
            if value.get_address() is not None and len(value.get_address()) > 0:
                return False
        if self.get_part_of() != value.get_part_of():
            return False
        effective_from = self.get_effective_from() 
        value_effective_from = value.get_effective_from()
        if effective_from is not None and value_effective_from is not None and effective_from.isostring != value_effective_from.isostring:
            return False
        effective_to = self.get_effective_to()
        value_effective_to = value.get_effective_to()
        if effective_to is not None and value_effective_to is not None and effective_to.isostring != value_effective_to.isostring:
            return False
        if self.get_contact_telecoms() is not None and len(self.get_contact_telecoms()) > 0:
            if value.get_contact_telecoms() is None or len(value.get_contact_telecoms()) == 0:
                return False
            for telecom in self.get_contact_telecoms():
                value_telecom_found = False
                for value_telecom in value.get_contact_telecoms():
                    if telecom.system == value_telecom.system and telecom.value == value_telecom.value and telecom.use == value_telecom.use:
                        value_telecom_found = True
                if not value_telecom_found:
                    return False
        if self.get_contact_address() is not None:
            if value.get_contact_address() is not None:
                return False
            if address.city == value_address.city and address.state == value_address.state and address.postalCode == value_address.postalCode and address.country == value_address.country:
                if address.line is None and value_address.line is not None:
                    return False
                if value_address.line is None and address.line is not None:
                    return False    
                for line in address.line:
                    if line not in value_address.line:
                        return False
        else:
            if value.get_contact_address() is not None:
                return False
        if self.is_active() != value.is_active():
            return False
        if self.get_version_id() != value.get_version_id():
            return False
        if self.get_contact() is not None and value.get_contact() is not None:
            for contact in self.get_contact():
                if contact.purpose is None or contact.purpose.coding is None or len(contact.purpose.coding) == 0:
                    break
                purpose_found = False
                for value_contact in value.get_contact():
                    if value_contact.purpose is None or value_contact.purpose.coding is None or len(value_contact.purpose.coding) == 0:
                        break
                    for code in contact.purpose.coding:
                        for value_code in value_contact.purpose.coding:
                            if code.code == value_code.code and code.display == value_code.display and code.system == value_code.system and code.version == value_code.version:
                                purpose_found = True
                                break
                if not purpose_found:
                    return False
        if len(self.get_mots_cles()) > 0:
            for mot_cle in self.get_mots_cles():
                if not value.have_mot_cle(mot_cle):
                    return False
        return True
    
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
    
    def __contains__(self, value: object) -> bool:
        if not isinstance(value, OrganizationVisitor):
            return False
        if value.get_id() is not None and self.get_id() != value.get_id():
            return False
        if value.get_name() is not None and self.get_name() != value.get_name():
            return False
        value_id_rrss = value.get_id_rrss()
        id_rrss = self.get_id_rrss()
        if value_id_rrss is not None and value_id_rrss != id_rrss:
            return False
        if value.get_id_hors_rrss() is not None and self.get_id_hors_rrss() != value.get_id_hors_rrss():
            return False
        if value.get_telecoms() is not None and len(value.get_telecoms()) > 0:
            if self.get_telecoms() is None or len(self.get_telecoms()) == 0:
                return False
            for value_telecom in value.get_telecoms():
                telcom_found = False
                for self_telecom in self.get_telecoms():
                    if (value_telecom.system is None or value_telecom.system == self_telecom.system) and \
                         (value_telecom.value is None or value_telecom.value == self_telecom.value) and \
                            (value_telecom.use is None or value_telecom.use == self_telecom.use):
                        telcom_found = True
                        break
                if not telcom_found:
                    return False
        if value.get_address() is not None and len(value.get_address()) > 0:
            for address in value.get_address():
                address_found = False
                for self_address in self.get_address():
                    if ((address.city is None or address.city == self_address.city) and \
                        (address.state is None or address.state == self_address.state) and \
                            (address.postalCode is None or address.postalCode == self_address.postalCode) and \
                                (address.country is None or address.country == self_address.country)):
                        if address.line is not None and len(address.line) > 0:
                            for line in address.line:
                                if line not in self_address.line:
                                    return False
                        address_found = True
                        break
                if not address_found:
                    return False
        if value.get_part_of() is not None and (self.get_part_of() is None or value.get_part_of().reference != self.get_part_of().reference):
            return False
        effective_from = self.get_effective_from() 
        value_effective_from = value.get_effective_from()
        if value_effective_from is not None:
            if effective_from is None or effective_from.isostring != value_effective_from.isostring:
                return False
        effective_to = self.get_effective_to()
        value_effective_to = value.get_effective_to()
        if value_effective_to is not None:
            if effective_to is None or effective_to.isostring != value_effective_to.isostring:
                return False
        if value.get_contact_telecoms() is not None and len(value.get_contact_telecoms()) > 0:
            for value_telecom in self.get_contact_telecoms():
                telcom_found = False
                for telecom in self.get_contact_telecoms():
                    if telecom.system == value_telecom.system and telecom.value == value_telecom.value and telecom.use == value_telecom.use:
                        telcom_found = True
                        break
                if not telcom_found:
                    return False
        if value.get_contact_address() is not None:
            if self.get_contact_address() is None:
                return False
            address = value.get_contact_address()
            self_address = self.get_contact_address()
            if address.city is not None and address.city != self_address.city:
                return False
            if address.state is not None and address.state != self_address.state:
                return False
            if address.postalCode is not None and address.postalCode != self_address.postalCode:
                return False
            if address.country is not None and address.country != self_address.country: 
                return False
            if address.line is not None and len(address.line) > 0:
                for line in address.line:
                    if line not in self_address.line:
                        return False
            else:
                return False

        if self.is_active() != value.is_active():
            return False
        if value.get_version_id() is not None and self.get_version_id() != value.get_version_id():
            return False
        if value.get_contact() is not None and self.get_contact() is not None:
            for value_contact in value.get_contact():
                purpose_found = False
                if value_contact.purpose is None or value_contact.purpose.coding is None or len(value_contact.purpose.coding) == 0:
                    break
                for contact in self.get_contact():
                    if contact.purpose is None or contact.purpose.coding is None or len(contact.purpose.coding) == 0:
                        break
                    for code in contact.purpose.coding:
                        for value_code in value_contact.purpose.coding:
                            if code.code == value_code.code and code.display == value_code.display and code.system == value_code.system and code.version == value_code.version:
                                purpose_found = True
                                break
                if not purpose_found:
                    return False
        if len(value.get_mots_cles()):
            for mot_cle in value.get_mots_cles():
                if not self.have_mot_cle(mot_cle):
                    return False
        return True

    def getFhirResource(self) -> Organization:
        return super().getFhirResource()  

    def get_id(self) -> str:
        return self.getFhirResource().id

    def set_version_id(self, versionId: int):
        if not self.getFhirResource().meta:
            self.getFhirResource().meta = Meta()
        self.getFhirResource().meta.versionId = versionId

    def get_version_id(self) -> int:
        if self.getFhirResource().meta:
            return self.getFhirResource().meta.versionId
        return None

    def get_identifier_by_system(self, system:str) -> str:
        if self.getFhirResource().identifier is not None:
            for identifier in self.getFhirResource().identifier:
                if identifier.system == system:
                    return identifier.value
        return None
    
    def get_id_rrss(self) -> str:
        return self.get_identifier_by_system(self.RRSS_SYSTEM)
    
    def get_id_hors_rrss(self) -> str:
        return self.get_identifier_by_system(self.HORS_RRSS_SYSTEM)
    
    def set_identifier_by_system(self, system:str, value:str):
        if self.getFhirResource().identifier is None:
            self.getFhirResource().identifier = []
        for identifier in self.getFhirResource().identifier:
            if identifier.system == system:
                identifier.value = value
                return
        identifier = Identifier()
        identifier.system = system
        identifier.value = value
        self.getFhirResource().identifier.append(identifier)

    def set_id_rrss(self, id_rrss:str):
        self.set_identifier_by_system(self.RRSS_SYSTEM, id_rrss)

    def set_id_hors_rrss(self, hors_rrss_id:str):
        self.set_identifier_by_system(self.HORS_RRSS_SYSTEM, hors_rrss_id)

    def set_name(self, name:str=None):
        self.getFhirResource().name = name

    def get_name(self) -> str:
        return self.getFhirResource().name

    def have_mot_cle(self, mot_cle=None) -> bool:
        if mot_cle is not None and self.getFhirResource().extension is not None:
            for extension in self.getFhirResource().extension:
                if extension.url == self.RRSS_MOT_CLE_EXTENSION_URL and extension.valueString == mot_cle:
                    return True
        return False

    def get_effective_from(self) -> FHIRDate:
        period_ext = self.__get_period_ext()
        if period_ext is not None and period_ext.valuePeriod is not None:
                return period_ext.valuePeriod.start
        return None

    def get_effective_to(self) -> FHIRDate:
        period_ext = self.__get_period_ext()
        if period_ext is not None and period_ext.valuePeriod is not None:
                return period_ext.valuePeriod.end
        return None

    def set_effective_from(self, effective_from=None):
        fhir_effective_from = None
        if type(effective_from) is str:
            fhir_effective_from = FHIRDate(jsonval=effective_from)
        elif type(effective_from) is FHIRDate:
            fhir_effective_from = effective_from
        period_ext = self.__get_period_ext()
        if period_ext is None or period_ext.valuePeriod is None:
            period = Period()
        else:
            period = period_ext.valuePeriod
        period.start = fhir_effective_from
        self.__set_period_ext(period=period)

    def set_effective_to(self, effective_to=None):
        fhir_effective_to = None
        if type(effective_to) is str:
            fhir_effective_to = FHIRDate(jsonval=effective_to)
        elif type(effective_to) is FHIRDate:
            fhir_effective_to = effective_to
        period_ext = self.__get_period_ext()
        if period_ext is None or period_ext.valuePeriod is None:
            period = Period()
        else:
            period = period_ext.valuePeriod
        period.end = fhir_effective_to
        self.__set_period_ext(period=period)

    def get_telecoms(self) -> list[ContactPoint]:
        return self.getFhirResource().telecom
    
    def set_telecoms(self, phones:list[ContactPoint]=None):
        self.getFhirResource().telecom = phones

    def get_phones(self) -> list[dict]:
        phones = []
        if self.getFhirResource().telecom is None:
            return phones
        for telecom in self.getFhirResource().telecom:
            if telecom.system == "phone":
                phone = {}
                phone["value"] = telecom.value
                phone["use"] = telecom.use
                phones.append(phone)
        return phones
    
    def set_phones(self, phones:list[dict]=None):
        if phones is not None:
            telecoms = []
            for phone in phones:
                telecom = ContactPoint()

                telecom.system = phone["system"] if "system" in phone else "phone"
                telecom.value = phone["value"]
                telecom.use = phone["use"] if "use" in phone else "work"

                telecoms.append(telecom)
            self.set_telecoms(telecoms)

    def add_telecom(self, phone:ContactPoint):
        if self.getFhirResource().telecom is None:
            self.getFhirResource().telecom = []
        self.getFhirResource().telecom.append(phone)

    def add_phone_by_fields(self, phone:dict):
        telecom = ContactPoint()
        telecom.system = phone["system"] if "system" in phone else "phone"
        telecom.value = phone["value"]
        telecom.use = phone["use"] if "use" in phone else "work"
        self.add_telecom(telecom)   

    def get_contact_telecoms(self) -> list[ContactPoint]:
        if self.getFhirResource().contact is not None and len(self.getFhirResource().contact) > 0:
            return self.getFhirResource().contact[0].telecom
        return []

    def set_contact_telecoms(self, telecoms: list[ContactPoint] = None):
        if self.getFhirResource().contact is None:
            self.getFhirResource().contact = [OrganizationContact()]
        elif len(self.getFhirResource().contact) == 0:
            self.getFhirResource().contact.append(OrganizationContact())
        self.getFhirResource().contact[0].telecom = telecoms

    def get_contacts_phones(self) -> list[dict]:
        phones = []
        if self.getFhirResource().contact is None:
            return phones
        for contact in self.getFhirResource().contact:
            for telecom in contact.telecom:
                if telecom.system == "phone":
                    phone = {}
                    phone["value"] = telecom.value
                    phone["use"] = telecom.use
                    phones.append(phone)
        return phones
    
    def get_contact(self) -> list[OrganizationContact]:
        return self.getFhirResource().contact

    def set_contact(self, contact: list[OrganizationContact] = None):
        self.getFhirResource().contact = contact

    def set_contacts_phones(self, phones: list[dict] = None):
        if phones is not None:
            if self.get_contact() is None:
                self.set_contact([OrganizationContact()])
            contact = self.get_contact()

            if contact[0].telecom is None:
                contact[0].telecom = []
            
            for phone in phones:
                telecom = ContactPoint()
                telecom.system = phone["system"] if "system" in phone else "phone"
                telecom.value = phone["value"]
                telecom.use = phone["use"] if "use" in phone else "work"

                contact[0].telecom.append(telecom)

    def add_contact_phone(self, phone: dict):
        contact = None
        if self.get_contact() is None:
            self.set_contact([OrganizationContact()])
        elif len(self.get.get_contact()) == 0:
            self.get_contact.contact().append(OrganizationContact())
        contact = self.get_contact()[0]

        telecom = ContactPoint()
        telecom.system = phone["system"] if "system" in phone else "phone"
        telecom.value = phone["value"]
        telecom.use = phone["use"] if "use" in phone else "work"
        if contact.telecom is None:
            contact.telecom = []
        contact.telecom.append(telecom)

    def set_contact_purpose_by_fields(self, code: str = None, display: str = None, system: str = None, version: str = None):
        if self.get_contact() is None:
            self.set_contact([OrganizationContact()])
        elif len(self.get.get_contact()) == 0:
            self.get_contact.contact().append(OrganizationContact())
        contact = self.get_contact()[0]
        purpose = self._to_codeable_concept(code=code, display=display, coding_system=system, coding_version=version)
        contact.purpose = purpose

    def get_contact_address(self) -> Address:
        if self.get_contact() is not None and len(self.get_contact()) > 0:
            return self.get_contact()[0].address
        return None

    def set_contact_address(self, address: Address = None):
        if self.get_contact() is None:
            self.set_contact([OrganizationContact()])
        elif len(self.get_contact()) == 0:
            self.get_contact().append(OrganizationContact())
        self.get_contact()[0].address = address

    def set_contact_address_by_fields(self, line:list=None, city:str=None, state:str=None, postal_code:str=None, country:str=None, type:str='physical', use:str='work'):
        address = Address()
        address.line = line
        address.city = city
        address.state = state
        address.postalCode = postal_code
        address.country = country
        address.type = type
        address.use = use
        self.set_contact_address(address)

    def is_active(self) -> bool:
        return self.getFhirResource().active
    
    def set_active(self, active: bool=True):
        self.getFhirResource().active = active

    def __get_period_ext(self) -> Extension:
        if self.getFhirResource().extension is not None:
            for ext in self.getFhirResource().extension:
                if ext.url == self.PERIOD_URL:
                    return ext
        return None

    def __set_period_ext(self, period:Period=None):
        if self.getFhirResource().extension is None:
            self.getFhirResource().extension = []
        period_ext = self.__get_period_ext()
        if period_ext is None:
            period_ext = Extension()
            period_ext.url = self.PERIOD_URL
            self.getFhirResource().extension.append(period_ext)
        period_ext.valuePeriod = period

    def get_address(self) -> Address:
        return self.getFhirResource().address

    def set_address(self, address:Address=None):
        self.getFhirResource().address = address

    def set_address_by_fields(self, line:list=None, city:str=None, state:str=None, postal_code:str=None, country:str=None):
        address = Address()
        address.line = line
        address.city = city
        address.state = state
        address.postalCode = postal_code
        address.country = country
        self.set_address(address)

    def get_part_of(self) -> Reference:
        return self.getFhirResource().partOf

    def set_part_of(self, part_of: Reference=None):
        self.getFhirResource().partOf = part_of

    def set_part_of_by_fields(self, part_of_id: str=None, part_of_display: str=None, part_of_ref: str=None):
        part_of_reference = Reference()
        part_of_reference.reference = f"Organization/{part_of_ref}"
        part_of_reference.display = part_of_display
        part_of_reference.id = part_of_id
        self.set_part_of(part_of_reference)

    def get_mots_cles(self) -> list[Extension]:
        mots_cles = []
        if self.getFhirResource().extension is not None:
            for ext in self.getFhirResource().extension:
                if ext.url == self.RRSS_MOT_CLE_EXTENSION_URL:
                    mots_cles.append(ext.valueString)
        return mots_cles