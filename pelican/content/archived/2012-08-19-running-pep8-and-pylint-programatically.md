Title: Running pep8 and pylint programatically
Date: 2012-08-19 15:12
Author: Attila-Mihaly Balazs
Tags: pylint, lint, python, pep8, static analysers
Slug: running-pep8-and-pylint-programatically
Status: published

Having tools like [pep8](http://pypi.python.org/pypi/pep8/) and
[pylint](http://pypi.python.org/pypi/pylint/) are great, especially
given the huge amount of dynamism involved in Python - which results in
many opportunities to shooting yourself in the foot. Sometimes however
you want to invoke these tools in more specialized ways, for example
only on the files which changed since the last commit. Here is how you
can do this from a python script and capture their output for later
post-processing (maybe you want merge the output from both tools, or
maybe you want to show only the lines which changed since the last
commit, etc):

    import pep8
    try:
      sys.stdout = StringIO()
      pep8_checker = pep8.StyleGuide(config_file=config, format='pylint')
      pep8_checker.check_files(paths=[ ...path to files/dirs to check... ])
      output = sys.stdout.getvalue()
    finally:
      sys.stdout = sys.__stdout__

    from pylint.lint import Run
    from pylint.reporters.text import ParseableTextReporter

    reporter = ParseableTextReporter()
    result = StringIO()
    reporter.set_output(result)
    Run(['--rcfile=pylint.config'] + [ ...files.., ], reporter=reporter, exit=False)
    output = result.getvalue()

</code>

It is recommended that you use pylint/pep8 installed trough
pip/easy\_install rather than the Linux distribution repositories, since
they are known to contain outdated software. You can check for this via
code like the following:

    if pkg_resources.get_distribution('pep8').parsed_version < parse_version('1.3.3'):
        logging.error('pep8 too old. At least version 1.3.3 is required')
        sys.exit(1)
    if pkg_resources.get_distribution('pylint').parsed_version < parse_version('0.25.1'):
        logging.error('pylint too old. At least version 0.25.1 is required')
        sys.exit(1)

</code>

Finally, if you *have* to use an old version of pep8, the code needs to
be modified to the following (however, this older version probably won't
be of much use and will most likely annoy you - you should really try to
use an up-to-date version - for example you could isolate this version
using virtualenv):

    result = []
    import pep8
    pep8.message = lambda msg: result.append(msg)
    pep8.process_options(own_code)
    for code_dir in [ ...files or dirs... ]:
        pep8.input_dir(code_dir)

</code>
