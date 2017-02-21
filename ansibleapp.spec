%if 0%{?fedora}
%global use_python3 1
%global use_python2 0
%global pythonbin %{__python3}
%global python_sitelib %{python3_sitelib}
%else
%global use_python3 0
%global use_python2 1
%if 0%{?__python2:1}
%global pythonbin %{__python2}
%global python_sitelib %{python2_sitelib}
%else
%global pythonbin %{__python}
%global python_sitelib %{python_sitelib}
%endif
%endif
%{!?python_sitelib: %define python_sitelib %(%{pythonbin} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: ansibleapp
Version: 0.1.0
Release: 1%{?dist}
Summary: A lightweight application definition (meta-containers)

Group: Development/Tools
License: GPLv2
URL: https://github.com/fusor/ansible-service-broker
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
%if %{use_python3}
#Requires: python3-pyparsing
Requires: python3-PyYAML
%else
#Requires: pyparsing
Requires: PyYAML
%endif

#%if 0%{?fedora}
## todo: add %check to spec file in accordance with
## https://fedoraproject.org/wiki/QA/Testing_in_check
#BuildRequires: git
#BuildRequires: python-bugzilla
#BuildRequires: python3-devel
#BuildRequires: python3-setuptools
#BuildRequires: python3-bugzilla
#BuildRequires: rpm-python3
#%endif

#Requires: rpm-build
#Requires: rpmlint
#Requires: fedpkg
#Requires: fedora-cert
#Requires: fedora-packager
#Requires: rpmdevtools
# Cheetah doesn't exist for Python 3, but it's what Mead uses.  We
# install it and call via the command line instead of importing the
# potentially incompatible code
#Requires: python-cheetah

%description
AnsibleApp is a lightweight application definition (meta-containers). AnsibleApp
has the following features:

%prep
%setup -q -n %{name}-%{version}
#sed -i 1"s|#!.*|#!%{pythonbin}|" bin/tito

%build
%{pythonbin} setup.py build
# convert manages
#a2x -d manpage -f manpage titorc.5.asciidoc
#a2x -d manpage -f manpage tito.8.asciidoc
#a2x -d manpage -f manpage tito.props.5.asciidoc
#a2x -d manpage -f manpage releasers.conf.5.asciidoc

%install
rm -rf $RPM_BUILD_ROOT
%{pythonbin} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
#rm -f $RPM_BUILD_ROOT%{python_sitelib}/*egg-info/requires.txt
## manpages
#%{__mkdir_p} %{buildroot}%{_mandir}/man5
#%{__mkdir_p} %{buildroot}%{_mandir}/man8
#cp -a titorc.5 tito.props.5 releasers.conf.5 %{buildroot}/%{_mandir}/man5/
#cp -a tito.8 %{buildroot}/%{_mandir}/man8/
## bash completion facilities
#install -Dp -m 0644 share/tito_completion.sh %{buildroot}%{_datadir}/bash-completion/completions/tito

%clean
rm -rf $RPM_BUILD_ROOT


%files
#%doc AUTHORS COPYING
#%doc doc/*
#%doc %{_mandir}/man5/titorc.5*
#%doc %{_mandir}/man5/tito.props.5*
#%doc %{_mandir}/man5/releasers.conf.5*
#%doc %{_mandir}/man8/tito.8*
%{_bindir}/ansibleapp
#%{_bindir}/generate-patches.pl
#%{_datadir}/bash-completion/completions/tito
%dir %{python_sitelib}/ansibleapp
%{python_sitelib}/ansibleapp/*
%{python_sitelib}/ansibleapp-*.egg-info


%changelog
