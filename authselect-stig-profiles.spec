Summary: Various authselect custom profiles to be compliant with the DISA STIG requirements
Name: authselect-stig-profiles
Version: 0.1
Release: 1
License: GPLv2+
URL: https://github.com/jfilizetti/authselect-stig-profiles
Source0: %{name}-%{version}.tgz
BuildArch: noarch
BuildRequires: authselect
BuildRequires: authselect-libs

# these are all static text files not code
%define __os_install_post %{nil}

%description
Set of custom authselect profiles which just modify the RHEL8 profiles to be
compliant with the DISA STIG

%prep

%build

%install
tar --strip-components=1 -C %{buildroot} -xf %{SOURCE0}

%files
%{_sysconfdir}/authselect/custom/*/*

%changelog
