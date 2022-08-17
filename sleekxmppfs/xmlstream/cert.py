import logging
from datetime import datetime, timedelta

# Make a call to strptime before starting threads to
# prevent thread safety issues.
datetime.strptime('1970-01-01 12:00:00', "%Y-%m-%d %H:%M:%S")

try:
    from packaging import version

    def check_version(ver1, ver2):
        return version.parse(ver1) <= version.parse(ver2)

except ImportError:
    from distutils.version import LooseVersion, StrictVersion

    def check_version(ver1, ver2):
        try:
            return StrictVersion(ver1) <= StrictVersion(ver2)
        except ValueError:
            return LooseVersion(ver1) <= LooseVersion(ver1)

try:
    from pyasn1 import __version__ as pyasn1_version
    from pyasn1.codec.der import decoder, encoder
    from pyasn1.type.univ import Any, ObjectIdentifier, OctetString
    from pyasn1.type.char import BMPString, IA5String, UTF8String
    from pyasn1.type.useful import GeneralizedTime
    from pyasn1_modules.rfc2459 import (Certificate, DirectoryString,
                                        SubjectAltName, GeneralNames,
                                        GeneralName)
    from pyasn1_modules.rfc2459 import id_ce_subjectAltName as SUBJECT_ALT_NAME
    from pyasn1_modules.rfc2459 import id_at_commonName as COMMON_NAME

    XMPP_ADDR = ObjectIdentifier('1.3.6.1.5.5.7.8.5')
    SRV_NAME = ObjectIdentifier('1.3.6.1.5.5.7.8.7')
    HAVE_PYASN1 = True
    HAVE_PYASN1_4 = check_version('0.4.1', pyasn1_version)
except ImportError:
    HAVE_PYASN1 = False
    HAVE_PYASN1_4 = False

log = logging.getLogger(__name__)


class CertificateError(Exception):
    pass


def decode_str(data):
    encoding = 'utf-16-be' if isinstance(data, BMPString) else 'utf-8'
    return bytes(data).decode(encoding)


def extract_names(raw_cert):
    results = {'CN': set(),
               'DNS': set(),
               'SRV': set(),
               'URI': set(),
               'XMPPAddr': set()}

    cert = decoder.decode(raw_cert, asn1Spec=Certificate())[0]
    tbs = cert.getComponentByName('tbsCertificate')
    subject = tbs.getComponentByName('subject')
    extensions = tbs.getComponentByName('extensions') or []

    # Extract the CommonName(s) from the cert.
    for rdnss in subject:
        for rdns in rdnss:
            for name in rdns:
                oid = name.getComponentByName('type')
                value = name.getComponentByName('value')

                if oid != COMMON_NAME:
                    continue

                value = decoder.decode(value, asn1Spec=DirectoryString())[0]
                value = decode_str(value.getComponent())
                results['CN'].add(value)

    # Extract the Subject Alternate Names (DNS, SRV, URI, XMPPAddr)
    for extension in extensions:
        oid = extension.getComponentByName('extnID')
        if oid != SUBJECT_ALT_NAME:
            continue

        if HAVE_PYASN1_4:
            value = extension.getComponentByName('extnValue')
        else:
            value = decoder.decode(
                extension.getComponentByName('extnValue'),
                asn1Spec=OctetString()
            )[0]

        sa_names = decoder.decode(value, asn1Spec=SubjectAltName())[0]
        for name in sa_names:
            name_type = name.getName()
            if name_type == 'dNSName':
                results['DNS'].add(decode_str(name.getComponent()))
            if name_type == 'uniformResourceIdentifier':
                value = decode_str(name.getComponent())
                if value.startswith('xmpp:'):
                    results['URI'].add(value[5:])
            elif name_type == 'otherName':
                name = name.getComponent()

                oid = name.getComponentByName('type-id')
                value = name.getComponentByName('value')

                if oid == XMPP_ADDR:
                    value = decoder.decode(value, asn1Spec=UTF8String())[0]
                    results['XMPPAddr'].add(decode_str(value))
                elif oid == SRV_NAME:
                    value = decoder.decode(value, asn1Spec=IA5String())[0]
                    results['SRV'].add(decode_str(value))

    return results


def extract_dates(raw_cert):
    # !!!! HACK HACK HACK HACK HACK !!!!
    # For this sucks-only version of SleekXMPP, we avoid validating the certs due to Ecovacs' servers having invalid certs
    return None, None

def get_ttl(raw_cert):
    not_before, not_after = extract_dates(raw_cert)
    if not_after is None:
        return None
    return not_after - datetime.utcnow()


def verify(expected, raw_cert):
    # !!!! HACK HACK HACK HACK HACK !!!!
    # For this sucks-only version of SleekXMPP, we avoid validating the certs due to Ecovacs' servers having invalid certs
    return
