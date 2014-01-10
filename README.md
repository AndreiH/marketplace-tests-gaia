Introduction
============

Marketplace is a Python package based on
[Gaia](https://github.com/mozilla-b2g/gaia).

Prerequisites
=============

You will need a
[Marionette enabled Firefox build](https://developer.mozilla.org/en-US/docs/Marionette/Builds)
that you can
[successfully connect to](https://developer.mozilla.org/en-US/docs/Marionette/Connecting_to_B2G).

Installation
============

Installation is simple:

    git clone https://github.com/mozilla/marketplace-tests-gaia.git
    cd marketplace-tests-gaia
    python setup.py develop

Risks
=====

Please visit [this page](https://developer.mozilla.org/en-US/docs/Gaia_Test_Runner) to understand and acknowledge the risks involved when running these tests.

Running Tests
=============

To run tests using gaia test, your command-line will vary a little bit
depending on what device you're using.  The general format is:

    gaiatest [options] /path/to/test_foo.py

Options:

    --emulator arm --homedir /path/to/emulator:  use these options to
        let Marionette launch an emulator for you in which to run a test
    --address <host>:<port>  use this option to run a test on an emulator
        which you've manually launched yourself, a real device, or a b2g
        desktop build.  If you've used port forwarding as described below,
        you'd specify --address localhost:2828
    --testvars= (see section below)
    --restart restart target instance between tests. This option will remove 
        the /data/local/indexedDB and /data/b2g/mozilla folders and restore the 
        device back to a common state

Testing on a Device
===================

You must run a build of B2G on the device that has Marionette enabled.
The easiest way to do that is to grab a nightly `eng` build, like
[this one for Unagi](https://pvtbuilds.mozilla.org/pub/mozilla.org/b2g/nightly/mozilla-b2g18-unagi-eng/latest/)
(currently it requires a Mozilla LDAP login). Flash that to your device.

You should not enable Remote Debugging manually on the device because
there will be competing debuggers. See
[bug 764913](https://bugzilla.mozilla.org/show_bug.cgi?id=764913).

If you are running the tests on a device connected via ADB (Android Debug
Bridge), you must additionally set up port forwarding from the device to your
local machine. You can do this by running the command:

    adb forward tcp:2828 tcp:2828

ADB is available in emulator packages under out/host/linux_x86/bin.
Alternatively, it may be downloaded as part of the
[Android SDK](http://developer.android.com/sdk/index.html).        

Test Variables
==============
We use the --testvars option to pass in local variables, particularly those that cannot be checked into the repository. For example in gaia-ui-tests these variables can be your private login credentials, phone number or details of your WiFi connection.

To use it, copy testvars_template.json to a different filename but add it into .gitignore so you don't check it into your repository.

When running your tests add the argument:
    --testvars=(filename).json

Variables:

    "settings": {},

    "wifi": {
        "ssid": ""
    },

    "marketplace": {
        "username": "",
        "password": ""
    }

Writing Tests
=============

Test writing for Marionette Python tests is described at
https://developer.mozilla.org/en-US/docs/Marionette/Marionette_Python_Tests.

At the moment we don't have a specific style guide. Please follow the
prevailing style of the existing tests. Use them as a template for writing
your tests.
We follow [PEP8](http://www.python.org/dev/peps/pep-0008/) for formatting, although we're pretty lenient on the
80-character line length.

