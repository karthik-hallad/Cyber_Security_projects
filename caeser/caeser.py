# Using deque from collections which has a better time complexity
import collections
import string


def caeser(st):

  csr=st.replace(" ","")
  for i in range(1,26):  
    upper=collections.deque(string.ascii_uppercase)
    lower=collections.deque(string.ascii_lowercase)
    upper.rotate(i)
    lower.rotate(i)
    upper=''.join(upper)
    lower=''.join(lower)
    print(csr.translate(csr.maketrans(string.ascii_uppercase,upper)).translate(csr.maketrans(string.ascii_lowercase,lower)))



st=input("Please Enter the text to be converted: \n")
print("The possible combinations are: ")
caeser(st)


#input
# Please Enter the text to be converted: 
# this is a test RUN PLZ BE CAREFUL OF CAESER

# output
# The possible combinations are:
# sghrhrzsdrsQTMOKYADBZQDETKNEBZDRDQ
# rfgqgqyrcqrPSLNJXZCAYPCDSJMDAYCQCP
# qefpfpxqbpqORKMIWYBZXOBCRILCZXBPBO
# pdeoeowpaopNQJLHVXAYWNABQHKBYWAOAN
# ocdndnvoznoMPIKGUWZXVMZAPGJAXVZNZM
# nbcmcmunymnLOHJFTVYWULYZOFIZWUYMYL
# mablbltmxlmKNGIESUXVTKXYNEHYVTXLXK
# lzakakslwklJMFHDRTWUSJWXMDGXUSWKWJ
# kyzjzjrkvjkILEGCQSVTRIVWLCFWTRVJVI
# jxyiyiqjuijHKDFBPRUSQHUVKBEVSQUIUH
# iwxhxhpithiGJCEAOQTRPGTUJADURPTHTG
# hvwgwgohsghFIBDZNPSQOFSTIZCTQOSGSF
# guvfvfngrfgEHACYMORPNERSHYBSPNRFRE
# ftueuemfqefDGZBXLNQOMDQRGXAROMQEQD
# estdtdlepdeCFYAWKMPNLCPQFWZQNLPDPC
# drscsckdocdBEXZVJLOMKBOPEVYPMKOCOB
# cqrbrbjcnbcADWYUIKNLJANODUXOLJNBNA
# bpqaqaibmabZCVXTHJMKIZMNCTWNKIMAMZ
# aopzpzhalzaYBUWSGILJHYLMBSVMJHLZLY
# znoyoygzkyzXATVRFHKIGXKLARULIGKYKX
# ymnxnxfyjxyWZSUQEGJHFWJKZQTKHFJXJW
# xlmwmwexiwxVYRTPDFIGEVIJYPSJGEIWIV
# wklvlvdwhvwUXQSOCEHFDUHIXORIFDHVHU
# vjkukucvguvTWPRNBDGECTGHWNQHECGUGT
# uijtjtbuftuSVOQMACFDBSFGVMPGDBFTFS
