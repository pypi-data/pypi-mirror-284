Generate release notes for the following git commit log messages.

commit aab33190d5f5633d5e835bf0baa4469687afa783
Author: Jeremy Nelson <jermnelson@gmail.com>
Date:   Thu May 9 12:20:22 2024 -0700

For MARC readers, initialize Leader class instead of string, which will make accessing and updating the MARC leader easier, and less error prone -- from @jermnelson
 
Test coverage on GitLab merge requests -- from @herrboyer

Adding MARCMakerReader for generating MARC data with textual format, previously pymarc only could generate records in this format -- from @herrboyer

 
commit d7ad0062c599642584b3035d8c8d0d9ea0746043
Author: Renaud Boyer <rboyer@anybox.fr>
Date:   Mon May 6 19:16:18 2024 +0200

    MARCMakerReader
    
    This commit adds a new class pymarc.str.MARCMakerReader for reading MARC records
    that are encoded using the MARCMaker format. Previously pymarc only had
    the ability to *write* records in this format.
    
    MARCMaker is human readable version of a MARC record, for example:
    
    ```text
    =LDR  01060cam  22002894a 4500
    =001  11778504
    =008  990802s2000\\\\mau\\\\\\b\\\\001\0\eng\\
    =050  00$aQA76.6$b.H857 2000
    =100  1\$aHunt, Andrew,$d1964-
    =245  14$aThe pragmatic programmer :$bfrom journeyman to master /$cAndrew Hunt, David Thomas.
    =260  \\$aReading, Mass :$bAddison-Wesley,$c2000.
    =300  \\$axxiv, 321 p. ;$c24 cm.
    =504  \\$aIncludes bibliographical references.
    =650  \0$aComputer programming.
    =700  1\$aThomas, David,$d1956-
    ```
    
    In order to read it you instantiate a MARCMakerReader object and use it
    as an iterator. For example, to get the first record:
    
    ```python
    from pymarc import MARCMakerReader
    
    rec = next(MARCMakerReader(open('record.mkr')))
    print(rec.title)
    ```
    
    It works similarl to MARCReader, but you don't open the file in binary
    mode, since it's assume to be a UTF-8 encoded string. You can change the
    encoding with the `encoding` parameter.

:100644 100644 7472b52 d00fffd M	docs/source/index.rst
:100644 100644 fd652eb 1e25af3 M	pymarc/reader.py
:100644 100644 224214a c1abf6e M	setup.cfg
:100644 100644 d54a5a9 7f6ab4e M	test/test_reader.py

commit ea843bfb177f6b8cdd7990976febda39a43545f6
Author: Andrew Hankinson <andrew.hankinson@gmail.com>
Date:   Sat May 4 18:54:11 2024 +0000

    Create Indicators type
    
    Previously, indicators of any length could be supplied with no checks on their length. This change introduces an "Indicators" named tuple that can only have two positions. If an iterable (list or tuple) of not exactly length two is passed, then a ValueError is now raised.
    
    The "old style" where a list of two elements are passed is still handled in the constructor; however, the type hints will indicate that this is not correct. (This is in preference to raising a Deprecation message). Internally this is coerced to the new named tuple type.
    
    If no indicator is passed, the value will be an indicator tuple with two space characters. As far as I can tell this was the default behaviour of pymarc previously.
    
    Tests are also updated to work with the new Indicator types, with tests for the old behaviour also added.
    
    Fixes #195

:100644 100644 38644ae 02b6213 M	.gitlab-ci.yml
:100644 100644 2b7e616 7ebc97c M	README.md
:100644 100644 82538e1 7fc524f M	README_pt_Br.md
:100644 100644 0982fc7 7472b52 M	docs/source/index.rst
:100644 100644 f9972f5 d554b58 M	pymarc/field.py
:100644 100644 4055ee8 776e447 M	pymarc/marc8.py
:100644 100644 fbb3445 2e6babc M	pymarc/marcjson.py
:100644 100644 e27ddce 2b72ae8 M	pymarc/marcxml.py
:100644 100644 fdd42ef fd652eb M	pymarc/reader.py
:100644 100644 83b880b ac9368f M	pymarc/record.py
:100644 100644 c5270fe 1c70b47 M	test/test_field.py
:100644 100644 5e62063 46c4b62 M	test/test_json.py
:100644 100644 a451151 348dcca M	test/test_marc8.py
:100644 100644 8260f81 e5d4e37 M	test/test_ordered_fields.py
:100644 100644 a123183 932e864 M	test/test_record.py
:100644 100644 45122cc a9684cf M	test/test_writer.py

commit 4ea33e9b2f50e0000d8a59f1aa175b7c9611fbef
Author: Andrew Hankinson <andrew.hankinson@gmail.com>
Date:   Tue Mar 26 18:04:17 2024 +0100

    Fixed: Raise KeyError for setitem
    
    To match __getitem__, __setitem__ now raises a KeyError for setting subfields on control fields.

:100644 100644 60e3596 f9972f5 M	pymarc/field.py

commit 6f88fc411d4890e399bcfa6378b75de3dc1e5606
Author: Andrew Hankinson <andrew.hankinson@gmail.com>
Date:   Tue Mar 26 15:35:23 2024 +0100

    Fixed: Iterating over fields fails
    
    Previously, iterating over fields and calling 'field.code' on the list of fields might fail, if the field was a control field.
    
    This was because `self.subfields` was only initialized if the field was not a control field, so it was attempting to iterate over an undefined property. For any blind iteration of all fields in a record, and all subfields in those fields, this raised an exception.
    
    To fix this, all fields are now pre-initialized in the init method, and updated with their value depending on the field status as a control field. Iterating over the subfields of a control field will no longer crash, but the list of subfields will be empty. Similarly, the `data` property is initialized to `None`, so accessing non-control fields' data property will also not crash.
    
    Additionally, the `is_control_field()` method has been refactored, and now takes its value from the `control_field` property set on initialization. This is because the nature of the field is set at init, so no need to re-check it.

:100644 100644 277701e 60e3596 M	pymarc/field.py
:100644 100644 f19c844 fbb3445 M	pymarc/marcjson.py
:100644 100644 8a4ca3b e27ddce M	pymarc/marcxml.py
:100644 100644 e6d6bdc 83b880b M	pymarc/record.py
:100644 100644 cf5e8d4 c5270fe M	test/test_field.py
:100644 100644 865cdab 8cab292 M	test/test_xml.py

commit 5265ccb48b75424dfadd9c79e7788ae554f7b8b9
Author: Benjamin Webb <bwebb@gpo.gov>
Date:   Fri Mar 22 09:46:37 2024 -0400

    Updated property name in docstrings

:100644 100644 2fc1d13 d01b429 M	pymarc/leader.py
