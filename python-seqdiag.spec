%define 	module	seqdiag
Summary:	seqkdiag generate sequence-diagram image file from spec-text file
Name:		python-%{module}
Version:	0.7.2
Release:	1
License:	Apache v2.0
Group:		Development/Languages
URL:		http://blockdiag.com/en/seqdiag/index.html
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	428341e76c3434ba3a87a063ca5fb721
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-blockdiag >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
seqdiag generates sequence-diagram image file from spec-text files.

Features:
- Generate sequence-diagram from dot like text (basic feature).
- Multilingualization for node-label (utf-8 only).

%prep
%setup -q -n %{module}-%{version}
%{__sed} -i -e 's/^from ez_setup/#from ez_setup/' setup.py
%{__sed} -i -e 's/^use_setuptools()/#use_setuptools()/' setup.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}_sphinxhelper.py[co]

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p %{module}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/seqdiag
%{_mandir}/man1/*.1*
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/utils
%{py_sitescriptdir}/%{module}/utils/*.py[co]
%dir %{py_sitescriptdir}/%{module}/utils/rst
%{py_sitescriptdir}/%{module}/utils/rst/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
%endif
