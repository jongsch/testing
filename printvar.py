import os

print "DOCKERFILE_TEST_VAR"
print os.environ.get("DOCKERFILE_TEST_VAR")
print "PRESETUP_TEST_VAR"
print os.environ.get("PRESETUP_TEST_VAR")
