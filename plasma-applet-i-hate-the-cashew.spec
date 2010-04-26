%define version 0.4
%define release %mkrel 2

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
