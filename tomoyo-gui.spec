Name:		tomoyo-gui
Version:	0.05
Release:	8
Summary:	Graphical interface for TOMOYO Linux
License:	GPLv2
Group:		System/Base
Url:		http://git.mandriva.com/?p=projects/tomoyo-mdv.git
Source0:	%{name}-%{version}.tar.bz2
Requires:	pygtk2.0
Requires:	python
Requires:	tomoyo-tools
BuildArch:	noarch

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
make install

%files
%doc AUTHORS COPYING README NEWS TODO
%{_sbindir}/tomoyo-gui
%{_datadir}/tomoyo-mdv/tomoyo-gui.*
%{_datadir}/tomoyo-mdv/version.*
%{_datadir}/tomoyo-mdv/tomoyo.png


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.05-4mdv2011.0
+ Revision: 670718
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.05-3mdv2011.0
+ Revision: 608038
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.05-2mdv2010.1
+ Revision: 524231
- rebuilt for 2010.1

* Thu Oct 01 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.05-1mdv2010.0
+ Revision: 452190
- 0.05:
- Implemented exception editing and deletion
- Implemented policy importing
- Support initializing tomoyo policy from toolbar

* Thu Sep 10 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.04-1mdv2010.0
+ Revision: 437498
- 0.04:
- Added help for all tabs
- Displaying exceptions in gui (read-only for now)
- Loading exceptions
- Creating initial tomoyo policy when necessary

* Wed Sep 09 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.03-1mdv2010.0
+ Revision: 435326
- 0.03:
- Show informative window when loading big tomoyo policy
- Handle cases when tomoyo policy was not correctly installed (#53382)

* Wed Jul 22 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.02-1mdv2010.0
+ Revision: 398692
- 0.02
- Implemented integration into MCC.
- Implemented partial policy exporting.

* Wed Jul 15 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.01-3mdv2010.0
+ Revision: 396074
- Use arch-specific libdir.
- First version. Use with care :).
- Created package structure for tomoyo-gui.

