%define version 0.3
%define release %mkrel 2

Name:		plasma-applet-i-hate-the-cashew
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:		http://www.kde.org/
Group:		Graphical desktop/KDE
Source0:	91009-iHateTheCashew-4.2.tbz
Patch0:		plasma-applet-ihatethecashew-fix-category.patch
Summary:	Plasmoid that remove the Cashew
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
Provides:	plasma-applet
Requires:	kdebase4-runtime

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
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
