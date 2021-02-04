# Created by pyp2rpm-3.3.5
%global pypi_name mrack

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Multicloud use-case based multihost async provisioner for CIs and testing during development

License:        Apache License 2.0
URL:            https://github.com/pvoborni/mrack
Source0:        %{pypi_source}
BuildArch:      noarch

### Patches ###
Patch0001:  0001-unset-boto-minimum-versions.patch

BuildRequires:  python3-devel
BuildRequires:  python3dist(asyncopenstackclient) >= 0.8.1
BuildRequires:  python3dist(beaker-client) >= 28
BuildRequires:  python3dist(boto3)
BuildRequires:  python3dist(botocore)
BuildRequires:  python3dist(click) >= 7
BuildRequires:  python3dist(pyyaml) >= 5
BuildRequires:  python3dist(setuptools)

%description
 ![pypi_badge]( ![readthedocs_badge]( most of the described below is not
implemented yetProvisioning library for CI and local multi-host testing
supporting multiple provisioning providers e.g. OpenStack, libvirt, containers,
Beaker).But in comparison to multi-cloud libraries, the aim is to be able to
describe host from application perspective. E.g.:yaml network: IPv4- name:...

%package -n     %{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide %{pypi_name}}

Requires:       python3dist(asyncopenstackclient) >= 0.8.1
Requires:       python3dist(beaker-client) >= 28
Requires:       python3dist(boto3)
Requires:       python3dist(botocore)
Requires:       python3dist(click) >= 7
Requires:       python3dist(pyyaml) >= 5
%description -n python3-%{pypi_name}
 ![pypi_badge]( ![readthedocs_badge]( most of the described below is not
implemented yetProvisioning library for CI and local multi-host testing
supporting multiple provisioning providers e.g. OpenStack, libvirt, containers,
Beaker).But in comparison to multi-cloud libraries, the aim is to be able to
describe host from application perspective. E.g.:yaml network: IPv4- name:...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/mrack
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Feb 04 2021 Armando Neto <abiagion@redhat.com> - 0.6.0-1
- Initial package.
