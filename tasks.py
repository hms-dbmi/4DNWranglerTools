# -*- coding: utf-8 -*-
import os
import sys
import webbrowser

from invoke import task, run

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')


@task
def test(ctx, watch=False, last_failing=False, no_flake=False):
    """Run the tests.
    Note: --watch requires pytest-xdist to be installed.
    """
    import pytest
    if not no_flake:
        flake(ctx)
    args = []
    if watch:
        args.append('-f')
    if last_failing:
        args.append('--lf')
    retcode = pytest.main(args)
    return(retcode)


@task
def flake(ctx):
    """Run flake8 on codebase."""
    run('flake8 .', echo=True)
    print("flake8 passed!!!")


@task
def clean(ctx):
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf 4DNWranglerTools.egg-info")
    clean_docs(ctx)
    print("Cleaned up.")


@task
def deploy(ctx, version=None):
    print("preparing for deploy...")
    print("first lets clean everythign up.")
    clean(ctx)
    print("now lets make sure the tests pass")
    test(ctx)
    print("next get version information")
    version = update_version(ctx, version)
    print("then tag the release in git")
    git_tag(ctx, version, "new production release %s" % (version))
    print("Build is now triggered for production deployment of %s "
          "check travis for build status" % (version))


@task
def update_version(ctx, version=None):
    from wranglertools._version import __version__
    print("Current version is ", __version__)
    if version is None:
        version = input("What version would you like to set for new release (please use x.x.x / "
                        " semantic versioning): ")

    # read the versions file
    lines = []
    with open("wranglertools/_version.py") as readfile:
        lines = readfile.readlines()

    if lines:
        with open("wranglertools/_version.py", 'w') as writefile:
            lines[-1] = '__version__ = "%s"\n' % (version.strip())
            writefile.writelines(lines)

    run("git add wranglertools/_version.py")
    run("git commit -m 'version bump'")
    print("version updated to", version)
    return version


@task
def git_tag(ctx, tag_name, msg):
    run('git tag -a %s -m "%s"' % (tag_name, msg))
    run('git push --tags')


@task
def clean_docs(ctx):
    run("rm -rf %s" % build_dir, echo=True)


@task
def browse_docs(ctx):
    path = os.path.join(build_dir, 'index.html')
    webbrowser.open_new_tab(path)


@task
def docs(ctx, clean=False, browse=False, watch=False):
    """Build the docs."""
    if clean:
        clean_docs()
    run("sphinx-build %s %s" % (docs_dir, build_dir), echo=True)
    if browse:
        browse_docs()
    if watch:
        watch_docs()


@task
def watch_docs(ctx):
    """Run build the docs when a file changes."""
    try:
        import sphinx_autobuild  # noqa
    except ImportError:
        print('ERROR: watch task requires the sphinx_autobuild package.')
        print('Install it with:')
        print('    pip install sphinx-autobuild')
        sys.exit(1)
    run('sphinx-autobuild {0} {1} --watch {2}'.format(
        docs_dir, build_dir, '4DNWranglerTools'), echo=True, pty=True)


@task
def readme(ctx, browse=False):
    run('rst2html.py README.rst > README.html')
    if browse:
        webbrowser.open_new_tab('README.html')


@task
def publish(ctx, test=False):
    """Publish to the cheeseshop."""
    clean(ctx)
    if test:
        run('python setup.py register -r test sdist bdist_wheel', echo=True)
        run('twine upload dist/* -r test', echo=True)
    else:
        run('python setup.py register sdist bdist_wheel', echo=True)
        run('twine upload dist/*', echo=True)
