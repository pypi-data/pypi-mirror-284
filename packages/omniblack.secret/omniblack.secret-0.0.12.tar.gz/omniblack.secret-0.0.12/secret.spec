%global project_name omniblack.secret
%global src_name %{project_name}
%global pkg_name %{py_dist_name %{project_name}}

Name: python-%{pkg_name}
Version: 0.0.12
Release: 1%{?dist}
Summary: Classes for safer handling of secrets in python.

License: MIT License
Source0: %{src_name}-%{version}.tar.gz

BuildRequires: python3-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: libsodium-devel
BuildRequires: libpasswdqc-devel

%description
Classes for safer handling of secrets. We use libsodium to
store secrets in memory that is protected by guard pages, a canary, and is set
to readonly when the library is not reading from it. These protections should
help mitigate exploits in other parts of the program allow for arbitrary reads
of memory, and should reduce the risk of buffer overflows and similar memory
writing...

%package -n     python3-%{pkg_name}
Summary:        %{summary}

%description -n python3-%{pkg_name}
Classes for safer handling of secrets. We use libsodium to
store secrets in memory that is protected by guard pages, a canary, and is set
to readonly when the library is not reading from it. These protections should
help mitigate exploits in other parts of the program allow for arbitrary reads
of memory, and should reduce the risk of buffer overflows and similar memory
writing...


%prep
%setup -n %{src_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install

%check
%py3_check_import %{project_name}
%pytest

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/omniblack/secret*
%{python3_sitearch}/%{project_name}-%{version}.dist-info/

%changelog
* Tue Jul 09 2024 Terry Patterson <Terryp@wegrok.net> - 0.0.11-1
- Initial package.
