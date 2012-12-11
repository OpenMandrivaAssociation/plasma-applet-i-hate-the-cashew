%define version 0.4
%define release %mkrel 3

Name:		plasma-applet-i-hate-the-cashew
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:		http://www.kde.org/
Group:		Graphical desktop/KDE
Source0:	http://www.kde-look.org/CONTENT/content-files/91009-iHateTheCashew-4.4.tbz
# Fix categories according to http://techbase.kde.org/Projects/Plasma/PIG#Category_Names
Patch0:		plasma-applet-ihatethecashew-0.4-mdv-fix-category.patch
Summary:	Plasmoid that remove the Cashew
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdebase4-workspace-devel
Requires:	kdebase4-runtime
Provides:	plasma-applet
  
%description 
Plasmoid that remove the Cashew

%files 
%defattr(-,root,root)
%doc COPYING
%_kde_libdir/kde4/plasma_applet_ihatethecashew.so
%_kde_services/plasma-applet-ihatethecashew.desktop

#-----------------------------------------------------------------------------

%prep
%setup -q -n iHateTheCashew
%patch0	-p0

%build
%cmake_kde4 
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%clean
%__rm -rf %buildroot


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdv2011.0
+ Revision: 614565
- the mass rebuild of 2010.1 packages

* Mon Apr 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4-2mdv2010.1
+ Revision: 538824
- Rebuild against latest kde4

* Sat Dec 19 2009 John Balcaen <mikala@mandriva.org> 0.4-1mdv2010.1
+ Revision: 480085
- Update to 0.4
- rename & rediff patch0
- clean spec

* Sun Sep 13 2009 John Balcaen <mikala@mandriva.org> 0.3-2mdv2010.0
+ Revision: 438592
- Fix applet category

* Mon Mar 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3-1mdv2009.1
+ Revision: 355931
- Fix version in fact this is  0.3

* Mon Mar 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.2-1mdv2009.1
+ Revision: 353139
- import plasma-applet-i-hate-the-cashew


