%define module dirty-equals
%define oname dirty_equals
# disable tests for abf
%bcond_with test

Name:		python-dirty-equals
Version:	0.9.0
Release:	1
Summary:	Doing dirty (but extremely useful) things with equals
URL:		https://pypi.org/project/dirty-equals/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/d/dirty-equals/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
%if %{with test}
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pydantic)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-examples)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(pytz)
%endif
Requires:	python%{pyver}dist(pytz) >= 2021.3

%description
Doing dirty (but extremely useful) things with equals.

dirty-equals is a python library that (mis)uses the __eq__ method to make
python code (generally unit tests) more declarative and therefore easier
to read and write.

dirty-equals can be used in whatever context you like, but it comes into
its own when writing unit tests for applications where you're commonly
checking the response to API calls and the contents of a database.

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
%{__python} -m pytest --import-mode append -v tests/
%endif

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
%license LICENSE
%doc README.md