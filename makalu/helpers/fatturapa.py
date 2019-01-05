from collections import defaultdict
from io import BytesIO
from base64 import b64decode
#from signxml import XMLVerifier
import xml.etree.ElementTree as ET

from makalu.models import Company

'''
RF = ('RF01', 'RF02', 'RF03', 'RF04', 'RF05', 'RF06', 'RF07', 'RF08', 'RF09', 'RF10',
      'RF11', 'RF12', 'RF13', 'RF14', 'RF15', 'RF16', 'RF17', 'RF18', 'RF19')
SU = ('SU', 'SM')
SL = ('LS', 'LN')
TD = map(lambda td: 'TD{:0=2d}'.format(td), range(1, 6))
TR = ['RT01','RT01']
TC = map(lambda tc: 'TC{:0=2d}'.format(tc), range(1,22))
NT = map(lambda nt: 'NT{:0=2d}'.format(nt), range(1,7))
TCP = ('SC', 'PR', 'AB', 'AC')
SM = ('SC', 'MG')
TP = ('TP01', 'TP02', 'TP03')
MP = map(lambda mp: 'MP{:0=2d}'.format(mp), range(1,22))
EI = ('I','D','S')
'''



class DynamicDict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

def float_to_str(number):
    return '{0:.2f}'.format(number)


#def verify_xml_sign(xmlfile):
#    cert = ET.parse(xmlfile).find('X509Certificate').text
#    assertion_data = XMLVerifier().verify(b64decode(assertion_body), x509_cert=cert).signed_xml


def get_company_data(element, fattura, primary=False):

    company = 'cessionariocommittente'
    if primary:
        company = 'cedenteprestatore'

    datianagrafici = element.find('DatiAnagrafici')
    if len(datianagrafici):
        id_fiscaleiva = datianagrafici.find('IdFiscaleIVA')
        if len(id_fiscaleiva):
            fattura['header'][company]['idfiscaleiva']['idpaese'] = id_fiscaleiva.find('IdPaese').text
            fattura['header'][company]['idfiscaleiva']['idcodice'] = id_fiscaleiva.find('IdCodice').text
            

        if primary:
            fattura['header'][company]['codicefiscale'] = datianagrafici.find('CodiceFiscale').text
            fattura['header'][company]['regimefiscale'] = datianagrafici.find('RegimeFiscale').text
        

        anagrafica = datianagrafici.find('Anagrafica')
        if len(anagrafica):
            fattura['header'][company]['anagrafica']['denominazione'] = anagrafica.find('Denominazione').text
            

    sede = element.find('Sede')
    if sede:
        fattura['header'][company]['sede']['indirizzo'] = sede.find('Indirizzo').text
        if sede.find('NumeroCivico'):
            fattura['header'][company]['sede']['numerocivico'] = sede.find('NumeroCivico').text
        else:
            fattura['header'][company]['sede']['numerocivico'] = ''
        fattura['header'][company]['sede']['cap'] = sede.find('CAP').text
        fattura['header'][company]['sede']['comune'] = sede.find('Comune').text  
        fattura['header'][company]['sede']['provincia'] = sede.find('Provincia').text
        fattura['header'][company]['sede']['nazione'] = sede.find('Nazione').text


def elaborate_xml(xmlfile):
    fattura = DynamicDict()
    root = ET.parse(xmlfile).getroot()

    # HEADER
    fatturaheader = root.find('FatturaElettronicaHeader')
    if len(fatturaheader):

        datitrasmissione = fatturaheader.find('DatiTrasmissione')

        if len(datitrasmissione):
            idtrasmittente = datitrasmissione.find('IdTrasmittente')
            if len(idtrasmittente):
                fattura['header']['datitrasmissione']['idpaese'] = idtrasmittente.find('IdPaese').text
                fattura['header']['datitrasmissione']['idcodice'] = idtrasmittente.find('IdCodice').text

                

            fattura['header']['datitrasmissione']['progressivoinvio'] = datitrasmissione.find('ProgressivoInvio').text
            fattura['header']['datitrasmissione']['formatotrasmissione'] =  datitrasmissione.find('FormatoTrasmissione').text
            fattura['header']['datitrasmissione']['codicedestinatario'] = datitrasmissione.find('CodiceDestinatario').text
            fattura['header']['datitrasmissione']['pecdestinatario'] = datitrasmissione.find('PECDestinatario').text

        

        cedenteprestatore = fatturaheader.find('CedentePrestatore')
        if len(cedenteprestatore):
            get_company_data(cedenteprestatore, fattura, True)
            

        cessionariocommittente = fatturaheader.find('CessionarioCommittente')
        if len(cessionariocommittente):
            get_company_data(cessionariocommittente, fattura)

    # END HEADER

    # BODY
    fatturabody = root.find('FatturaElettronicaBody')
    if len(fatturabody):
        datigenerali = fatturabody.find('DatiGenerali')
        if len(datigenerali):
            datigeneralidocumento = datigenerali.find('DatiGeneraliDocumento')
            if len(datigeneralidocumento):
                fattura['body']['datigenerali']['datigeneralidocumento']['tipodocumento'] = datigeneralidocumento.find('TipoDocumento').text
                fattura['body']['datigenerali']['datigeneralidocumento']['divisa'] = datigeneralidocumento.find('Divisa').text
                fattura['body']['datigenerali']['datigeneralidocumento']['data'] = datigeneralidocumento.find('Data').text
                fattura['body']['datigenerali']['datigeneralidocumento']['numero'] = datigeneralidocumento.find('Numero').text
                fattura['body']['datigenerali']['datigeneralidocumento']['importototaledocumento'] = datigeneralidocumento.find('ImportoTotaleDocumento').text

        datibeniservizi = fatturabody.find('DatiBeniServizi')
        if len(datibeniservizi):
            fattura['body']['datibeniservizi']['dettagliolinee'] = []
            dettagliolinee = datibeniservizi.findall('DettaglioLinee')
            for item in dettagliolinee:
                fattura['body']['datibeniservizi']['dettagliolinee'].append({
                    'numerolinea': item.find('NumeroLinea').text,
                    'descrizione': item.find('Descrizione').text,
                    'quantita': item.find('Quantita').text,
                    'prezzounitario': item.find('PrezzoUnitario').text,
                    'prezzototale': item.find('PrezzoTotale').text,
                    'aliquotaiva': item.find('AliquotaIVA').text
                })
            
            datidiriepilogo = datibeniservizi.find('DatiRiepilogo')
            if len(datidiriepilogo):
                fattura['body']['datiriepilogo']['aliquotaiva'] = datidiriepilogo.find('AliquotaIVA').text
                fattura['body']['datiriepilogo']['imponibileimporto'] = datidiriepilogo.find('ImponibileImporto').text
                fattura['body']['datiriepilogo']['imposta'] = datidiriepilogo.find('Imposta').text

    return fattura




def get_fatturapa_xml(fattura):
    root = ET.Element("ns2:FatturaElettronica")
    root.set('versione', 'FPR12')
    root.set('xmlns:ns2', 'http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2')


    header = ET.SubElement(root, 'FatturaElettronicaHeader')
    datitrasmissione = ET.SubElement(header, 'DatiTrasmissione')
    idtrasmittente = ET.SubElement(datitrasmissione, 'IdTrasmittente')

    ET.SubElement(idtrasmittente, "IdPaese").text = fattura['transmission_country']
    ET.SubElement(idtrasmittente, "IdCodice").text = fattura['user'].fiscal_code

    ET.SubElement(datitrasmissione, 'ProgressivoInvio').text = str(fattura['transmission_progressive'])
    ET.SubElement(datitrasmissione, 'FormatoTrasmissione').text = fattura['transmission_format']
    ET.SubElement(datitrasmissione, 'CodiceDestinatario').text = fattura['commissioned'].code
    ET.SubElement(datitrasmissione, 'PECDestinatario').text = fattura['commissioned'].pec


    company = Company.objects.get(primary=True)
    cedenteprestatore = ET.SubElement(header, 'CedentePrestatore')
    cedentedatianagrafici = ET.SubElement(cedenteprestatore, 'DatiAnagrafici')
    cedenteidfiscaleiva = ET.SubElement(cedentedatianagrafici, 'IdFiscaleIVA')

    ET.SubElement(cedenteidfiscaleiva, 'IdPaese').text = company.country
    ET.SubElement(cedenteidfiscaleiva, 'IdCodice').text = company.vat_code

    ET.SubElement(cedentedatianagrafici, 'CodiceFiscale').text = company.fiscal_code
    ET.SubElement(cedentedatianagrafici, 'RegimeFiscale').text = company.fiscal_type
    cedenteanagrafica = ET.SubElement(cedentedatianagrafici, 'Anagrafica')
    ET.SubElement(cedenteanagrafica, 'Denominazione').text = company.name

    cedentesede = ET.SubElement(cedenteprestatore, 'Sede')
    ET.SubElement(cedentesede, 'Indirizzo').text = company.address
    ET.SubElement(cedentesede, 'NumeroCivico').text = company.address_number
    ET.SubElement(cedentesede, 'CAP').text = company.zip_code
    ET.SubElement(cedentesede, 'Comune').text = company.city
    ET.SubElement(cedentesede, 'Provincia').text = company.province
    ET.SubElement(cedentesede, 'Nazione').text = company.country


    cessionariocommittente = ET.SubElement(header, 'CessionarioCommittente')
    cessionariodatianagrafici = ET.SubElement(cessionariocommittente, 'DatiAnagrafici')
    cessionarioidfiscaleiva = ET.SubElement(cessionariodatianagrafici, 'IdFiscaleIVA')

    ET.SubElement(cessionarioidfiscaleiva, 'IdPaese').text = fattura['commissioned'].country
    ET.SubElement(cessionarioidfiscaleiva, 'IdCodice').text = fattura['commissioned'].vat_code

    #ET.SubElement(cedentedatianagrafici, 'CodiceFiscale').text = company.fiscal_code
    
    cessionarioanagrafica = ET.SubElement(cessionariodatianagrafici, 'Anagrafica')
    ET.SubElement(cessionarioanagrafica, 'Denominazione').text = fattura['commissioned'].name

    cessionariosede = ET.SubElement(cessionariocommittente, 'Sede')
    ET.SubElement(cessionariosede, 'Indirizzo').text = fattura['commissioned'].address
    ET.SubElement(cessionariosede, 'NumeroCivico').text = fattura['commissioned'].address_number
    ET.SubElement(cessionariosede, 'CAP').text = fattura['commissioned'].zip_code
    ET.SubElement(cessionariosede, 'Comune').text = fattura['commissioned'].city
    ET.SubElement(cessionariosede, 'Provincia').text = fattura['commissioned'].province
    ET.SubElement(cessionariosede, 'Nazione').text = fattura['commissioned'].country


    body = ET.SubElement(root, 'FatturaElettronicaBody')
    datigenerali = ET.SubElement(body, 'DatiGenerali')
    datigeneralidocumento = ET.SubElement(datigenerali, 'DatiGeneraliDocumento')

    ET.SubElement(datigeneralidocumento, 'TipoDocumento').text = fattura['invoice_type']
    ET.SubElement(datigeneralidocumento, 'Divisa').text = fattura['currency']
    ET.SubElement(datigeneralidocumento, 'Data').text = fattura['date'].strftime('%Y-%m-%d')
    ET.SubElement(datigeneralidocumento, 'Numero').text = str(fattura['number'])
    ET.SubElement(datigeneralidocumento, 'ImportoTotaleDocumento').text = float_to_str(fattura['total'] + (fattura['tax_rate'] * fattura['total']) / 100)

    riepilogo = []
    datibeniservizi = ET.SubElement(body, 'DatiBeniServizi')
    for item in fattura['rows']:
        dettagliolinee = ET.SubElement(datibeniservizi, 'DettaglioLinee')
        ET.SubElement(dettagliolinee, 'NumeroLinea').text = str(item.number)
        ET.SubElement(dettagliolinee, 'Descrizione').text = item.description
        ET.SubElement(dettagliolinee, 'Quantita').text = str(item.quantity)
        ET.SubElement(dettagliolinee, 'PrezzoUnitario').text = float_to_str(item.unit_price)
        ET.SubElement(dettagliolinee, 'PrezzoTotale').text = float_to_str(item.total_price)
        ET.SubElement(dettagliolinee, 'AliquotaIVA').text = float_to_str(item.tax_rate)

        rr_added = False
        for ritem in riepilogo:
            if ritem['al'] == item.tax_rate:
                ritem['to'] = ritem['to'] + item.total_price
                ritem['tx'] = ritem['tx'] + (item.tax_rate * item.total_price / 100)
                rr_added = True
               
        if not riepilogo or not rr_added:
            riepilogo.append({
                'al': item.tax_rate,
                'to': item.total_price,
                'tx': item.tax_rate
            })
    
    rtotal = 0
    for ritem in riepilogo:
        datiriepilogo = ET.SubElement(datibeniservizi, 'DatiRiepilogo')
        ET.SubElement(datiriepilogo, 'AliquotaIVA').text = float_to_str(ritem['al'])
        ET.SubElement(datiriepilogo, 'ImponibileImporto').text = float_to_str(ritem['to'])
        ET.SubElement(datiriepilogo, 'Imposta').text = float_to_str(ritem['tx'])

        rtotal = rtotal + (ritem['to'] + ritem['tx'])

    ET.SubElement(datigeneralidocumento, 'ImportoTotaleDocumento').text = float_to_str(rtotal)


    tree = ET.ElementTree(root)

    xml = BytesIO()
    tree.write(xml, encoding='utf-8', xml_declaration=True) 
    
    return xml