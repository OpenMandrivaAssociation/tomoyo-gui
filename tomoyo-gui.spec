Name:		tomoyo-gui
Version:	0.05
Release:	%mkrel 4
Summary:	Graphical interface for TOMOYO Linux
License:	GPLv2
Group:		System/Base
Url:		http://git.mandriva.com/?p=projects/tomoyo-mdv.git
Source0:	%{name}-%{version}.tar.bz2
Requires:	pygtk2.0
Requires:	python
Requires:	ccs-tools
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is the graphical interface to TOMOYO Linux Security Framework,
developed by Mandriva. This GUI allows to view and edit system security
policy, and create custom set of profiles for individual applications in a
similar way to AppArmor security framework.

%prep
%setup -q

%build
make all

%install
rm -rf %{buildroot}

make install

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS TODO
%_sbindir/tomoyo-gui
%_datadir/tomoyo-mdv/tomoyo-gui.*
%_datadir/tomoyo-mdv/version.*
%_datadir/tomoyo-mdv/tomoyo.png
