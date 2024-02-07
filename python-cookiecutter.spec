# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-cookiecutter
Epoch: 100
Version: 2.4.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Command-line utility that creates projects from cookiecutters
License: BSD-3-Clause
URL: https://github.com/cookiecutter/cookiecutter/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-cookiecutter
Summary: Command-line utility that creates projects from cookiecutters
Requires: python3
Requires: python3-arrow
Requires: python3-binaryornot >= 0.4.4
Requires: python3-click >= 7.0
Requires: python3-Jinja2 >= 2.7
Requires: python3-PyYAML >= 5.3.1
Requires: python3-requests >= 2.23.0
Requires: python3-rich
Requires: python3-slugify >= 4.0.0
Provides: python3-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python3dist(cookiecutter) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cookiecutter) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cookiecutter) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-cookiecutter
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

%files -n python%{python3_version_nodots}-cookiecutter
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-cookiecutter
Summary: Command-line utility that creates projects from cookiecutters
Requires: python3
Requires: python3-arrow
Requires: python3-binaryornot >= 0.4.4
Requires: python3-click >= 7.0
Requires: python3-Jinja2 >= 2.7
Requires: python3-PyYAML >= 5.3.1
Requires: python3-requests >= 2.23.0
Requires: python3-rich
Requires: python3-slugify >= 4.0.0
Provides: python3-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python3dist(cookiecutter) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cookiecutter) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cookiecutter) = %{epoch}:%{version}-%{release}

%description -n python3-cookiecutter
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

%files -n python3-cookiecutter
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-cookiecutter
Summary: Command-line utility that creates projects from cookiecutters
Requires: python3
Requires: python3-arrow
Requires: python3-binaryornot >= 0.4.4
Requires: python3-click >= 7.0
Requires: python3-jinja2 >= 2.7
Requires: python3-pyyaml >= 5.3.1
Requires: python3-requests >= 2.23.0
Requires: python3-rich
Requires: python3-slugify >= 4.0.0
Provides: python3-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python3dist(cookiecutter) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cookiecutter) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cookiecutter = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cookiecutter) = %{epoch}:%{version}-%{release}

%description -n python3-cookiecutter
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

%files -n python3-cookiecutter
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
