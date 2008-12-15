%define name	nagios-check_zone_auth
%define version	1.9
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check DNS zones synchronisation
Group:		Networking/Other
License:	BSD
URL:		http://dns.measurement-factory.com/tools/nagios-plugins/check_zone_auth.html
Source0:	http://dns.measurement-factory.com/tools/nagios-plugins/src/check_zone_auth
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Use this plugin with Nagios to make sure that the authoritative nameservers for
a given zone remain in sync.

%prep

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_zone_auth.cfg <<'EOF'
define command{
	command_name	check_zone_auth
	command_line	%{_datadir}/nagios/plugins/check_zone_auth -Z $HOSTADDRESS$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_zone_auth
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_zone_auth.cfg
