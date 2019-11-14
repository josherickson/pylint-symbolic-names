# Pylint Symbolic Names

The list of symbolic names for every pylint message, which are particularly useful for disabling warnings in a readable way such as `#pylint: disable=missing-docstring` rather than `#pylint: disable=C0111`.

This list was automatically generated using [generate.py](generate.py). You can also get the list of messages yourself with the built-in pylint command `pylint --list-msgs`.

_pylint version: 2.4.4_

| Code | Symbolic Name | Message |
| ---- |-------------- | ------- |
| C0102 | `blacklisted-name` | Black listed name "%s" |
| C0103 | `invalid-name` | %s name "%s" doesn't conform to %s |
| C0112 | `empty-docstring` | Empty %s docstring |
| C0113 | `unneeded-not` | Consider changing "%s" to "%s" |
| C0114 | `missing-module-docstring` | Missing module docstring |
| C0115 | `missing-class-docstring` | Missing class docstring |
| C0116 | `missing-function-docstring` | Missing function or method docstring |
| C0121 | `singleton-comparison` | Comparison to %s should be %s |
| C0122 | `misplaced-comparison-constant` | Comparison should be %s |
| C0123 | `unidiomatic-typecheck` | Using type() instead of isinstance() for a typecheck. |
| C0200 | `consider-using-enumerate` | Consider using enumerate instead of iterating with range and len |
| C0201 | `consider-iterating-dictionary` | Consider iterating the dictionary directly instead of calling .keys() |
| C0202 | `bad-classmethod-argument` | Class method %s should have %s as first argument |
| C0203 | `bad-mcs-method-argument` | Metaclass method %s should have %s as first argument |
| C0204 | `bad-mcs-classmethod-argument` | Metaclass class method %s should have %s as first argument |
| C0205 | `single-string-used-for-slots` | Class \_\_slots\_\_ should be a non-string iterable |
| C0301 | `line-too-long` | Line too long (%s/%s) |
| C0302 | `too-many-lines` | Too many lines in module (%s/%s) |
| C0303 | `trailing-whitespace` | Trailing whitespace |
| C0304 | `missing-final-newline` | Final newline missing |
| C0305 | `trailing-newlines` | Trailing newlines |
| C0321 | `multiple-statements` | More than one statement on a single line |
| C0325 | `superfluous-parens` | Unnecessary parens after %r keyword |
| C0326 | `bad-whitespace` | %s space %s %s %s %s |
| C0327 | `mixed-line-endings` | Mixed line endings LF and CRLF |
| C0328 | `unexpected-line-ending-format` | Unexpected line ending format. There is '%s' while it should be '%s'. |
| C0330 | `bad-continuation` | Wrong %s indentation%s%s. %s%s |
| C0401 | `wrong-spelling-in-comment` | Wrong spelling of a word '%s' in a comment: %s %s Did you mean: '%s'? |
| C0402 | `wrong-spelling-in-docstring` | Wrong spelling of a word '%s' in a docstring: %s %s Did you mean: '%s'? |
| C0403 | `invalid-characters-in-docstring` | Invalid characters %r in a docstring |
| C0410 | `multiple-imports` | Multiple imports on one line (%s) |
| C0411 | `wrong-import-order` | %s should be placed before %s |
| C0412 | `ungrouped-imports` | Imports from package %s are not grouped |
| C0413 | `wrong-import-position` | Import "%s" should be placed at the top of the module |
| C0414 | `useless-import-alias` | Import alias does not rename original package |
| C0415 | `import-outside-toplevel` | Import outside toplevel (%s) |
| C1801 | `len-as-condition` | Do not use \`len(SEQUENCE)\` without comparison to determine if a sequence is empty |
| E0100 | `init-is-generator` | \_\_init\_\_ method is a generator |
| E0101 | `return-in-init` | Explicit return in \_\_init\_\_ |
| E0102 | `function-redefined` | %s already defined line %s |
| E0103 | `not-in-loop` | %r not properly in loop |
| E0104 | `return-outside-function` | Return outside function |
| E0105 | `yield-outside-function` | Yield outside function |
| E0106 | `return-arg-in-generator` | Return with argument inside generator |
| E0107 | `nonexistent-operator` | Use of the non-existent %s operator |
| E0108 | `duplicate-argument-name` | Duplicate argument name %s in function definition |
| E0110 | `abstract-class-instantiated` | Abstract class %r with abstract methods instantiated |
| E0111 | `bad-reversed-sequence` | The first reversed() argument is not a sequence |
| E0112 | `too-many-star-expressions` | More than one starred expression in assignment |
| E0113 | `invalid-star-assignment-target` | Starred assignment target must be in a list or tuple |
| E0114 | `star-needs-assignment-target` | Can use starred expression only in assignment target |
| E0115 | `nonlocal-and-global` | Name %r is nonlocal and global |
| E0116 | `continue-in-finally` | 'continue' not supported inside 'finally' clause |
| E0117 | `nonlocal-without-binding` | nonlocal name %s found without binding |
| E0118 | `used-prior-global-declaration` | Name %r is used prior to global declaration |
| E0119 | `misplaced-format-function` | format function is not called on str |
| E0202 | `method-hidden` | An attribute defined in %s line %s hides this method |
| E0203 | `access-member-before-definition` | Access to member %r before its definition line %s |
| E0211 | `no-method-argument` | Method has no argument |
| E0213 | `no-self-argument` | Method should have "self" as first argument |
| E0236 | `invalid-slots-object` | Invalid object %r in \_\_slots\_\_, must contain only non empty strings |
| E0237 | `assigning-non-slot` | Assigning to attribute %r not defined in class slots |
| E0238 | `invalid-slots` | Invalid \_\_slots\_\_ object |
| E0239 | `inherit-non-class` | Inheriting %r, which is not a class. |
| E0240 | `inconsistent-mro` | Inconsistent method resolution order for class %r |
| E0241 | `duplicate-bases` | Duplicate bases for class %r |
| E0242 | `class-variable-slots-conflict` | Value %r in slots conflicts with class variable |
| E0301 | `non-iterator-returned` | \_\_iter\_\_ returns non-iterator |
| E0302 | `unexpected-special-method-signature` | The special method %r expects %s param(s), %d %s given |
| E0303 | `invalid-length-returned` | \_\_len\_\_ does not return non-negative integer |
| E0401 | `import-error` | Unable to import %s |
| E0402 | `relative-beyond-top-level` | Attempted relative import beyond top-level package |
| E0601 | `used-before-assignment` | Using variable %r before assignment |
| E0602 | `undefined-variable` | Undefined variable %r |
| E0603 | `undefined-all-variable` | Undefined variable name %r in \_\_all\_\_ |
| E0604 | `invalid-all-object` | Invalid object %r in \_\_all\_\_, must contain only strings |
| E0611 | `no-name-in-module` | No name %r in module %r |
| E0633 | `unpacking-non-sequence` | Attempting to unpack a non-sequence%s |
| E0701 | `bad-except-order` | Bad except clauses order (%s) |
| E0702 | `raising-bad-type` | Raising %s while only classes or instances are allowed |
| E0703 | `bad-exception-context` | Exception context set to something which is not an exception, nor None |
| E0704 | `misplaced-bare-raise` | The raise statement is not inside an except clause |
| E0710 | `raising-non-exception` | Raising a new style class which doesn't inherit from BaseException |
| E0711 | `notimplemented-raised` | NotImplemented raised - should raise NotImplementedError |
| E0712 | `catching-non-exception` | Catching an exception which doesn't inherit from Exception: %s |
| E1003 | `bad-super-call` | Bad first argument %r given to super() |
| E1101 | `no-member` | %s %r has no %r member%s |
| E1102 | `not-callable` | %s is not callable |
| E1111 | `assignment-from-no-return` | Assigning result of a function call, where the function has no return |
| E1120 | `no-value-for-parameter` | No value for argument %s in %s call |
| E1121 | `too-many-function-args` | Too many positional arguments for %s call |
| E1123 | `unexpected-keyword-arg` | Unexpected keyword argument %r in %s call |
| E1124 | `redundant-keyword-arg` | Argument %r passed by position and keyword in %s call |
| E1125 | `missing-kwoa` | Missing mandatory keyword argument %r in %s call |
| E1126 | `invalid-sequence-index` | Sequence index is not an int, slice, or instance with \_\_index\_\_ |
| E1127 | `invalid-slice-index` | Slice index is not an int, None, or instance with \_\_index\_\_ |
| E1128 | `assignment-from-none` | Assigning result of a function call, where the function returns None |
| E1129 | `not-context-manager` | Context manager '%s' doesn't implement \_\_enter\_\_ and \_\_exit\_\_. |
| E1130 | `invalid-unary-operand-type` | %s |
| E1131 | `unsupported-binary-operation` | %s |
| E1132 | `repeated-keyword` | Got multiple values for keyword argument %r in function call |
| E1133 | `not-an-iterable` | Non-iterable value %s is used in an iterating context |
| E1134 | `not-a-mapping` | Non-mapping value %s is used in a mapping context |
| E1135 | `unsupported-membership-test` | Value '%s' doesn't support membership test |
| E1136 | `unsubscriptable-object` | Value '%s' is unsubscriptable |
| E1137 | `unsupported-assignment-operation` | %r does not support item assignment |
| E1138 | `unsupported-delete-operation` | %r does not support item deletion |
| E1139 | `invalid-metaclass` | Invalid metaclass %r used |
| E1140 | `unhashable-dict-key` | Dict key is unhashable |
| E1141 | `dict-iter-missing-items` | Unpacking a dictionary in iteration without calling .items() |
| E1200 | `logging-unsupported-format` | Unsupported logging format character %r (%#02x) at index %d |
| E1201 | `logging-format-truncated` | Logging format string ends in middle of conversion specifier |
| E1205 | `logging-too-many-args` | Too many arguments for logging format string |
| E1206 | `logging-too-few-args` | Not enough arguments for logging format string |
| E1300 | `bad-format-character` | Unsupported format character %r (%#02x) at index %d |
| E1301 | `truncated-format-string` | Format string ends in middle of conversion specifier |
| E1302 | `mixed-format-string` | Mixing named and unnamed conversion specifiers in format string |
| E1303 | `format-needs-mapping` | Expected mapping for format string, not %s |
| E1304 | `missing-format-string-key` | Missing key %r in format string dictionary |
| E1305 | `too-many-format-args` | Too many arguments for format string |
| E1306 | `too-few-format-args` | Not enough arguments for format string |
| E1307 | `bad-string-format-type` | Argument %r does not match format type %r |
| E1310 | `bad-str-strip-call` | Suspicious argument in %s.%s call |
| E1507 | `invalid-envvar-value` | %s does not support %s type argument |
| E1601 | `print-statement` | print statement used |
| E1602 | `parameter-unpacking` | Parameter unpacking specified |
| E1603 | `unpacking-in-except` | Implicit unpacking of exceptions is not supported in Python 3 |
| E1604 | `old-raise-syntax` | Use raise ErrorClass(args) instead of raise ErrorClass, args. |
| E1605 | `backtick` | Use of the \`\` operator |
| E1606 | `long-suffix` | Use of long suffix |
| E1607 | `old-ne-operator` | Use of the <> operator |
| E1608 | `old-octal-literal` | Use of old octal literal |
| E1609 | `import-star-module-level` | Import \* only allowed at module level |
| E1610 | `non-ascii-bytes-literal` | Non-ascii bytes literals not supported in 3.x |
| E1700 | `yield-inside-async-function` | Yield inside async function |
| E1701 | `not-async-context-manager` | Async context manager '%s' doesn't implement \_\_aenter\_\_ and \_\_aexit\_\_. |
| F0202 | `method-check-failed` | Unable to check methods signature (%s / %s) |
| I0023 | `use-symbolic-message-instead` | %s |
| I1101 | `c-extension-no-member` | %s %r has no %r member%s, but source is unavailable. Consider adding this module to extension-pkg-whitelist if you want to perform analysis based on run-time introspection of living objects. |
| R0123 | `literal-comparison` | Comparison to literal |
| R0124 | `comparison-with-itself` | Redundant comparison - %s |
| R0201 | `no-self-use` | Method could be a function |
| R0202 | `no-classmethod-decorator` | Consider using a decorator instead of calling classmethod |
| R0203 | `no-staticmethod-decorator` | Consider using a decorator instead of calling staticmethod |
| R0205 | `useless-object-inheritance` | Class %r inherits from object, can be safely removed from bases in python3 |
| R0206 | `property-with-parameters` | Cannot have defined parameters for properties |
| R0401 | `cyclic-import` | Cyclic import (%s) |
| R0801 | `duplicate-code` | Similar lines in %s files %s |
| R0901 | `too-many-ancestors` | Too many ancestors (%s/%s) |
| R0902 | `too-many-instance-attributes` | Too many instance attributes (%s/%s) |
| R0903 | `too-few-public-methods` | Too few public methods (%s/%s) |
| R0904 | `too-many-public-methods` | Too many public methods (%s/%s) |
| R0911 | `too-many-return-statements` | Too many return statements (%s/%s) |
| R0912 | `too-many-branches` | Too many branches (%s/%s) |
| R0913 | `too-many-arguments` | Too many arguments (%s/%s) |
| R0914 | `too-many-locals` | Too many local variables (%s/%s) |
| R0915 | `too-many-statements` | Too many statements (%s/%s) |
| R0916 | `too-many-boolean-expressions` | Too many boolean expressions in if statement (%s/%s) |
| R1701 | `consider-merging-isinstance` | Consider merging these isinstance calls to isinstance(%s, (%s)) |
| R1702 | `too-many-nested-blocks` | Too many nested blocks (%s/%s) |
| R1703 | `simplifiable-if-statement` | The if statement can be replaced with %s |
| R1704 | `redefined-argument-from-local` | Redefining argument with the local name %r |
| R1705 | `no-else-return` | Unnecessary "%s" after "return" |
| R1706 | `consider-using-ternary` | Consider using ternary (%s) |
| R1707 | `trailing-comma-tuple` | Disallow trailing comma tuple |
| R1708 | `stop-iteration-return` | Do not raise StopIteration in generator, use return statement instead |
| R1709 | `simplify-boolean-expression` | Boolean expression may be simplified to %s |
| R1710 | `inconsistent-return-statements` | Either all return statements in a function should return an expression, or none of them should. |
| R1711 | `useless-return` | Useless return at end of function or method |
| R1712 | `consider-swap-variables` | Consider using tuple unpacking for swapping variables |
| R1713 | `consider-using-join` | Consider using str.join(sequence) for concatenating strings from an iterable |
| R1714 | `consider-using-in` | Consider merging these comparisons with "in" to %r |
| R1715 | `consider-using-get` | Consider using dict.get for getting values from a dict if a key is present or a default if not |
| R1716 | `chained-comparison` | Simplify chained comparison between the operands |
| R1717 | `consider-using-dict-comprehension` | Consider using a dictionary comprehension |
| R1718 | `consider-using-set-comprehension` | Consider using a set comprehension |
| R1719 | `simplifiable-if-expression` | The if expression can be replaced with %s |
| R1720 | `no-else-raise` | Unnecessary "%s" after "raise" |
| R1721 | `unnecessary-comprehension` | Unnecessary use of a comprehension |
| R1722 | `consider-using-sys-exit` | Consider using sys.exit() |
| R1723 | `no-else-break` | Unnecessary "%s" after "break" |
| R1724 | `no-else-continue` | Unnecessary "%s" after "continue" |
| W0101 | `unreachable` | Unreachable code |
| W0102 | `dangerous-default-value` | Dangerous default value %s as argument |
| W0104 | `pointless-statement` | Statement seems to have no effect |
| W0105 | `pointless-string-statement` | String statement has no effect |
| W0106 | `expression-not-assigned` | Expression "%s" is assigned to nothing |
| W0107 | `unnecessary-pass` | Unnecessary pass statement |
| W0108 | `unnecessary-lambda` | Lambda may not be necessary |
| W0109 | `duplicate-key` | Duplicate key %r in dictionary |
| W0111 | `assign-to-new-keyword` | Name %s will become a keyword in Python %s |
| W0120 | `useless-else-on-loop` | Else clause on loop without a break statement |
| W0122 | `exec-used` | Use of exec |
| W0123 | `eval-used` | Use of eval |
| W0124 | `confusing-with-statement` | Following "as" with another context manager looks like a tuple. |
| W0125 | `using-constant-test` | Using a conditional statement with a constant value |
| W0126 | `missing-parentheses-for-call-in-test` | Using a conditional statement with potentially wrong function or method call due to missing parentheses |
| W0127 | `self-assigning-variable` | Assigning the same variable %r to itself |
| W0128 | `redeclared-assigned-name` | Redeclared variable %r in assignment |
| W0143 | `comparison-with-callable` | Comparing against a callable, did you omit the parenthesis? |
| W0150 | `lost-exception` | %s statement in finally block may swallow exception |
| W0199 | `assert-on-tuple` | Assert called on a 2-item-tuple. Did you mean 'assert x,y'? |
| W0201 | `attribute-defined-outside-init` | Attribute %r defined outside \_\_init\_\_ |
| W0211 | `bad-staticmethod-argument` | Static method with %r as first argument |
| W0212 | `protected-access` | Access to a protected member %s of a client class |
| W0221 | `arguments-differ` | Parameters differ from %s %r method |
| W0222 | `signature-differs` | Signature differs from %s %r method |
| W0223 | `abstract-method` | Method %r is abstract in class %r but is not overridden |
| W0231 | `super-init-not-called` | \_\_init\_\_ method from base class %r is not called |
| W0232 | `no-init` | Class has no \_\_init\_\_ method |
| W0233 | `non-parent-init-called` | \_\_init\_\_ method from a non direct base class %r is called |
| W0235 | `useless-super-delegation` | Useless super delegation in method %r |
| W0236 | `invalid-overridden-method` | Method %r was expected to be %r, found it instead as %r |
| W0301 | `unnecessary-semicolon` | Unnecessary semicolon |
| W0311 | `bad-indentation` | Bad indentation. Found %s %s, expected %s |
| W0312 | `mixed-indentation` | Found indentation with %ss instead of %ss |
| W0401 | `wildcard-import` | Wildcard import %s |
| W0402 | `deprecated-module` | Uses of a deprecated module %r |
| W0404 | `reimported` | Reimport %r (imported line %s) |
| W0406 | `import-self` | Module import itself |
| W0407 | `preferred-module` | Prefer importing %r instead of %r |
| W0410 | `misplaced-future` | \_\_future\_\_ import is not the first non docstring statement |
| W0511 | `fixme` | %s |
| W0601 | `global-variable-undefined` | Global variable %r undefined at the module level |
| W0602 | `global-variable-not-assigned` | Using global for %r but no assignment is done |
| W0603 | `global-statement` | Using the global statement |
| W0604 | `global-at-module-level` | Using the global statement at the module level |
| W0611 | `unused-import` | Unused %s |
| W0612 | `unused-variable` | Unused variable %r |
| W0613 | `unused-argument` | Unused argument %r |
| W0614 | `unused-wildcard-import` | Unused import %s from wildcard import |
| W0621 | `redefined-outer-name` | Redefining name %r from outer scope (line %s) |
| W0622 | `redefined-builtin` | Redefining built-in %r |
| W0623 | `redefine-in-handler` | Redefining name %r from %s in exception handler |
| W0631 | `undefined-loop-variable` | Using possibly undefined loop variable %r |
| W0632 | `unbalanced-tuple-unpacking` | Possible unbalanced tuple unpacking with sequence%s: left side has %d label(s), right side has %d value(s) |
| W0640 | `cell-var-from-loop` | Cell variable %s defined in loop |
| W0641 | `possibly-unused-variable` | Possibly unused variable %r |
| W0642 | `self-cls-assignment` | Invalid assignment to %s in method |
| W0702 | `bare-except` | No exception type(s) specified |
| W0703 | `broad-except` | Catching too general exception %s |
| W0705 | `duplicate-except` | Catching previously caught exception type %s |
| W0706 | `try-except-raise` | The except handler raises immediately |
| W0711 | `binary-op-exception` | Exception to catch is the result of a binary "%s" operation |
| W0715 | `raising-format-tuple` | Exception arguments suggest string formatting might be intended |
| W0716 | `wrong-exception-operation` | Invalid exception operation. %s |
| W1113 | `keyword-arg-before-vararg` | Keyword argument before variable positional arguments list in the definition of %s function |
| W1114 | `arguments-out-of-order` | Positional arguments appear to be out of order |
| W1201 | `logging-not-lazy` | Specify string format arguments as logging function parameters |
| W1202 | `logging-format-interpolation` | Use %s formatting in logging functions%s |
| W1300 | `bad-format-string-key` | Format string dictionary key should be a string, not %s |
| W1301 | `unused-format-string-key` | Unused key %r in format string dictionary |
| W1302 | `bad-format-string` | Invalid format string |
| W1303 | `missing-format-argument-key` | Missing keyword argument %r for format string |
| W1304 | `unused-format-string-argument` | Unused format argument %r |
| W1305 | `format-combined-specification` | Format string contains both automatic field numbering and manual field specification |
| W1306 | `missing-format-attribute` | Missing format attribute %r in format specifier %r |
| W1307 | `invalid-format-index` | Using invalid lookup key %r in format specifier %r |
| W1308 | `duplicate-string-formatting-argument` | Duplicate string formatting argument %r, consider passing as named argument |
| W1401 | `anomalous-backslash-in-string` | Anomalous backslash in string: '%s'. String constant might be missing an r prefix. |
| W1402 | `anomalous-unicode-escape-in-string` | Anomalous Unicode escape in byte string: '%s'. String constant might be missing an r or u prefix. |
| W1403 | `implicit-str-concat-in-sequence` | Implicit string concatenation found in %s |
| W1501 | `bad-open-mode` | "%s" is not a valid mode for open. |
| W1502 | `boolean-datetime` | Using datetime.time in a boolean context. |
| W1503 | `redundant-unittest-assert` | Redundant use of %s with constant value %r |
| W1505 | `deprecated-method` | Using deprecated method %s() |
| W1506 | `bad-thread-instantiation` | threading.Thread needs the target function |
| W1507 | `shallow-copy-environ` | Using copy.copy(os.environ). Use os.environ.copy() instead.  |
| W1508 | `invalid-envvar-default` | %s default type is %s. Expected str or None. |
| W1509 | `subprocess-popen-preexec-fn` | Using preexec\_fn keyword which may be unsafe in the presence of threads |
| W1510 | `subprocess-run-check` | Using subprocess.run without explicitly set \`check\` is not recommended. |
| W1601 | `apply-builtin` | apply built-in referenced |
| W1602 | `basestring-builtin` | basestring built-in referenced |
| W1603 | `buffer-builtin` | buffer built-in referenced |
| W1604 | `cmp-builtin` | cmp built-in referenced |
| W1605 | `coerce-builtin` | coerce built-in referenced |
| W1606 | `execfile-builtin` | execfile built-in referenced |
| W1607 | `file-builtin` | file built-in referenced |
| W1608 | `long-builtin` | long built-in referenced |
| W1609 | `raw_input-builtin` | raw\_input built-in referenced |
| W1610 | `reduce-builtin` | reduce built-in referenced |
| W1611 | `standarderror-builtin` | StandardError built-in referenced |
| W1612 | `unicode-builtin` | unicode built-in referenced |
| W1613 | `xrange-builtin` | xrange built-in referenced |
| W1614 | `coerce-method` | \_\_coerce\_\_ method defined |
| W1615 | `delslice-method` | \_\_delslice\_\_ method defined |
| W1616 | `getslice-method` | \_\_getslice\_\_ method defined |
| W1617 | `setslice-method` | \_\_setslice\_\_ method defined |
| W1618 | `no-absolute-import` | import missing \`from \_\_future\_\_ import absolute\_import\` |
| W1619 | `old-division` | division w/o \_\_future\_\_ statement |
| W1620 | `dict-iter-method` | Calling a dict.iter\*() method |
| W1621 | `dict-view-method` | Calling a dict.view\*() method |
| W1622 | `next-method-called` | Called a next() method on an object |
| W1623 | `metaclass-assignment` | Assigning to a class's \_\_metaclass\_\_ attribute |
| W1624 | `indexing-exception` | Indexing exceptions will not work on Python 3 |
| W1625 | `raising-string` | Raising a string exception |
| W1626 | `reload-builtin` | reload built-in referenced |
| W1627 | `oct-method` | \_\_oct\_\_ method defined |
| W1628 | `hex-method` | \_\_hex\_\_ method defined |
| W1629 | `nonzero-method` | \_\_nonzero\_\_ method defined |
| W1630 | `cmp-method` | \_\_cmp\_\_ method defined |
| W1632 | `input-builtin` | input built-in referenced |
| W1633 | `round-builtin` | round built-in referenced |
| W1634 | `intern-builtin` | intern built-in referenced |
| W1635 | `unichr-builtin` | unichr built-in referenced |
| W1636 | `map-builtin-not-iterating` | map built-in referenced when not iterating |
| W1637 | `zip-builtin-not-iterating` | zip built-in referenced when not iterating |
| W1638 | `range-builtin-not-iterating` | range built-in referenced when not iterating |
| W1639 | `filter-builtin-not-iterating` | filter built-in referenced when not iterating |
| W1640 | `using-cmp-argument` | Using the cmp argument for list.sort / sorted |
| W1641 | `eq-without-hash` | Implementing \_\_eq\_\_ without also implementing \_\_hash\_\_ |
| W1642 | `div-method` | \_\_div\_\_ method defined |
| W1643 | `idiv-method` | \_\_idiv\_\_ method defined |
| W1644 | `rdiv-method` | \_\_rdiv\_\_ method defined |
| W1645 | `exception-message-attribute` | Exception.message removed in Python 3 |
| W1646 | `invalid-str-codec` | non-text encoding used in str.decode |
| W1647 | `sys-max-int` | sys.maxint removed in Python 3 |
| W1648 | `bad-python3-import` | Module moved in Python 3 |
| W1649 | `deprecated-string-function` | Accessing a deprecated function on the string module |
| W1650 | `deprecated-str-translate-call` | Using str.translate with deprecated deletechars parameters |
| W1651 | `deprecated-itertools-function` | Accessing a deprecated function on the itertools module |
| W1652 | `deprecated-types-field` | Accessing a deprecated fields on the types module |
| W1653 | `next-method-defined` | next method defined |
| W1654 | `dict-items-not-iterating` | dict.items referenced when not iterating |
| W1655 | `dict-keys-not-iterating` | dict.keys referenced when not iterating |
| W1656 | `dict-values-not-iterating` | dict.values referenced when not iterating |
| W1657 | `deprecated-operator-function` | Accessing a removed attribute on the operator module |
| W1658 | `deprecated-urllib-function` | Accessing a removed attribute on the urllib module |
| W1659 | `xreadlines-attribute` | Accessing a removed xreadlines attribute |
| W1660 | `deprecated-sys-function` | Accessing a removed attribute on the sys module |
| W1661 | `exception-escape` | Using an exception object that was bound by an except handler |
| W1662 | `comprehension-escape` | Using a variable that was bound inside a comprehension |
