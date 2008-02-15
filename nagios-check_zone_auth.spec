%define name	nagios-check_zone_auth
%define version	1.1
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check DNS zones synchronisation
Group:		Networking/Other
License:	BSD
URL:		http://dns.measurement-factory.com/tools/nagios-plugins/check_zone_auth.html
Source0:	http://dns.measurement-factory.com/tools/nagios-plugins/src/check_zone_auth
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Use this plugin with Nagios to make sure that the authoritative nameservers for
a given zone remain in sync.

%prep

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_libdir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_libdir}/nagios/plugins

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/nagios/plugins/check_zone_auth
