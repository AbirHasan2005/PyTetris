# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwoKIyBGaWxlOiBjb25zdGFudHMucHkgCiMgRGVzY3JpcHRpb246IEJhc2ljIHByb2dyYW0gY29uc3RhbnRzLgojIEF1dGhvcjogUGF2ZWwgQmVuw6HEjWVrIDxwYXZlbC5iZW5hY2VrQGdtYWlsLmNvbT4KCiMgVGhpcyBwcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU6IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkKIyBpdCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGFzIHB1Ymxpc2hlZCBieQojIHRoZSBGcmVlIFNvZnR3YXJlIEZvdW5kYXRpb24sIGVpdGhlciB2ZXJzaW9uIDMgb2YgdGhlIExpY2Vuc2UsIG9yCiMgKGF0IHlvdXIgb3B0aW9uKSBhbnkgbGF0ZXIgdmVyc2lvbi4KIyAKIyBUaGlzIHByb2dyYW0gaXMgZGlzdHJpYnV0ZWQgaW4gdGhlIGhvcGUgdGhhdCBpdCB3aWxsIGJlIHVzZWZ1bCwKIyBidXQgV0lUSE9VVCBBTlkgV0FSUkFOVFk7IHdpdGhvdXQgZXZlbiB0a'
love = 'THtnJ1joTyyMPO3LKWlLJ50rFOiMtbwVR1SHxAVDH5HDHWWGRyHJFOipvOTFIEBEIAGVRMCHvOOVSOOHyEWD1IZDIVtHSIFHR9GEF4tVSAyMFO0nTHXVlOUGyHtE2IhMKWuoPODqJWfnJZtGTywMJ5mMFOzo3VtoJ9lMFOxMKEunJkmYtbwVNbwVSyiqFOmnT91oTDtnTS2MFOlMJAynKMyMPOuVTAipUxto2LtqTuyVRqBIFOUMJ5ypzSfVSO1LzkcLlOZnJAyoaAyPvZtLJkiozptq2y0nPO0nTymVUOlo2qlLJ0hVPOWMvOho3DfVUAyMFN8nUE0pQbiY3q3ql5aoaHho3WaY2kcL2Ihp2ImYm4hPtbXMaWioFOjrJquoJHhoT9wLJkmVTygpT9lqPNdPtbwVRAiozMcM3IlLKEco24to2LtLaIcoTEcozptp2uupTHtLzkiL2fXVlOKnJE0nPOiMvO0nTHtp2uupTHtLzkiL2fXDyqWESEVVPNtVPN9VQVjPvZtFTIcM2u0VT9zVUEbMFOmnTSjMFOvoT9wnjcPFRIWE0uHVPNtVQ0tZwNXVlOKnJE0nPOiMvO0nTHtoTyhMFOupz91ozDtqTuyVTWfo2AePx1SH0usI0yRIRttCFNkPtbwVRAiozMcM3IlLK'
god = 'Rpb24gb2YgdGhlIHBsYXllciBib2FyZAojIEJvYXJkIGxpbmUgaGVpZ2h0CkJPQVJEX0hFSUdIVCAgICAgPSA3CiMgTWFyZ2luIG9mIHVwcGVyIGxpbmUgKGZvciBzY29yZSkKQk9BUkRfVVBfTUFSR0lOICA9IDQwCiMgTWFyZ2lucyBhcm91bmQgYWxsIGxpbmVzCkJPQVJEX01BUkdJTiAgICAgPSAyCgojIENvbG9yIGRlY2xhcmF0aW9ucyBpbiB0aGUgUkdCIG5vdGF0aW9uCldISVRFICAgID0gKDI1NSwyNTUsMjU1KQpSRUQgICAgICA9ICgyNTUsMCwwKQpHUkVFTiAgICA9ICgwLDI1NSwwKQpCTFVFICAgICA9ICgwLDAsMjU1KQpPUkFOR0UgICA9ICgyNTUsNjksMCkKR09MRCAgICAgPSAoMjU1LDEyNSwwKQpQVVJQTEUgICA9ICgxMjgsMCwxMjgpCkNZQU4gICAgID0gKDAsMjU1LDI1NSkgCkJMQUNLICAgID0gKDAsMCwwKQoKIyBUaW1pbmcgY29uc3RyYWludHMKIyBUaW1lIGZvciB0aGUgZ2VuZXJhdGlvbiBvZiBUSU1FX01PVkVfRVZFTlQgKG1zKQpNT1ZFX1RJQ0sgICAgICA'
destiny = 'tVPNtCFNkZQNjPvZtDJkfo2AuqTIxVT51oJWypvOzo3VtqTuyVT1iqzHtMT93o24tMKMyoaDXIRyAEIWsGH9JEI9SIxIBIPNtVQ0tIIASHxIJEH5HXmRXVlOGpTIyMPO1pPOlLKEcolOiMvO0nTHtM2SgMFNbnJ50MJqypvO2LJk1MKZcPxqOGHIsH1OSEHEIHS9FDIEWGlN9VQRhADbwVSAwo3WyVRkSIxIZVP0tMzylp3DtqTulMKAbo2kxVT9zVUEbMFOmL29lMDcGD09FEI9ZEIMSGPNtVPNtVPNtCFNlZQNjPvZtH2AipzHtoTI2MJjtpzS0nJ8XH0ACHxIsGRIJEHksHxSHFH8tVQ0tZvNXPvZtD29hMzyaqKWuqTyiovOiMvOmL29lMDbwVR51oJWypvOiMvOjo2yhqUZtMz9lVT9hMFOvqJyfMTyhMlOvoT9wnjcDG0yBIS9JDHkIEFNtVPNtVPN9VQRjZNbwVR1upzqcovOiMvO0nTHtH0ACHxHtp3ElnJ5aPyOCFH5HK01OHxqWGvNtVPNtVQ0tZGNXPvZtEz9hqPOmnKcyVTMipvOuoTjtp3ElnJ5aplNbp2AipzHfVUOuqKAyYPOaLJ1yVT92MKVcPxMCGyEsH0ynEFNtVPNtVPNtVPNtCFNlADb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))