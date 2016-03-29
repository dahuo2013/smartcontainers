import pytest
import os
import sc

def test_appendData():
    #Create scMetadata instance
    scmd = sc.scMetadata.scMetadata()
    #Create a temporary file to append to.
    scmd.createLDPContainer("~/justfortest", "testfolder")
    assert os.path.exists("~/justfortest/.meta")