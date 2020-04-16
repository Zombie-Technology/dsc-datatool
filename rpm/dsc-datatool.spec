Name:           dsc-datatool
Version:        1.0.0
Release:        1%{?dist}
Summary:        Export DSC data to other formats and/or databases
Group:          Productivity/Networking/DNS/Utilities

License:        BSD-3-Clause
URL:            https://www.dns-oarc.net/oarc/data/dsc
# Source needs to be generated by dist-tools/create-source-packages, see
# https://github.com/jelu/dist-tools
Source0:        https://github.com/DNS-OARC/dsc-datatool/archive/v%{version}.tar.gz?/%{name}_%{version}.orig.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if 0%{?suse_version} || 0%{?sle_version}
BuildRequires:  python3-maxminddb
BuildRequires:  python3-PyYAML
%else
BuildRequires:  python36-maxminddb
BuildRequires:  python36-PyYAML
%endif

%if 0%{?suse_version} || 0%{?sle_version}
Requires:       python3-maxminddb
Requires:       python3-PyYAML
%else
Requires:       python36-maxminddb
Requires:       python36-PyYAML
%endif

%package doc
Summary:        Documentation files for %{name}
Group:          Documentation


%description
Tool for converting, exporting, merging and transforming DSC data.


%description doc
Tool for converting, exporting, merging and transforming DSC data.

This package contains the documentation for dsc-datatool.


%prep
%setup -q -n %{name}_%{version}


%build
python3 setup.py build


%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}


%files
%license LICENSE
%{_bindir}/dsc-datatool
%{python3_sitelib}/dsc_datatool*


%files doc
%doc CHANGES README.md UPGRADE.md
%license LICENSE


%changelog
* Wed Apr 15 2020 Jerry Lundström <lundstrom.jerry@gmail.com> 1.0.0-1
- Prepare for v1.0.0
* Fri May 31 2019 Jerry Lundström <lundstrom.jerry@gmail.com> 0.05-1
- Release 0.05
  * Fixed issue with empty values in InfluxDB output, they are now
    quoted as an empty string.
  * Commits:
    9917c4e InfluxDB quote keys/values
* Mon Jan 21 2019 Jerry Lundström <lundstrom.jerry@gmail.com> 0.04-1
- Release 0.04
  * Package dependency fix and update of example Grafana dashboards.
  * Commits:
    d3babc9 Copyright years
    9955c88 Travis Perl versions
    134a8b3 Debian dependency
    2d2114d Fix #23: Rework Grafana dashboards to hopefully show more
            correct numbers and also split them up.
    9bca0d3 Prepare SPEC for OSB/COPR
* Fri Dec 16 2016 Jerry Lundström <lundstrom.jerry@gmail.com> 0.03-1
- Release 0.03
  * Support processing of 25 of the 37 DAT files that the Extractor
    can produce, the others can not be converted into time series data
    since they lack timestamps.  Processing of XML is the recommended
    approach to secure all information.
  * Commits:
    72e829c Implement processing of DAT directories
    45294d0 RPM spec
    4e8ff69 Fix 5.24 forbidden keys usage
    7589ad2 Use perl 5.24 also
    cfac110 Fix #16: Handle directories in --xml and warn that --dat is
            not implemented yet
* Thu Dec 15 2016 Jerry Lundström <lundstrom.jerry@gmail.com> 0.02-1
- Initial package
