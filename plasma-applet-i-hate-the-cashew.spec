%define version  0.2
%define release  %mkrel 1 

Name:		 plasma-applet-i-hate-the-cashew
Version:	 %{version}
Release:	 %{release}
License:	 GPLv2+
Url:		 http://www.kde.org/ 
Group:		 Graphical desktop/KDE
Source0:	     91009-iHateTheCashew-4.2.tbz
Summary:         Plasmoid that remove the Cashew
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:   kdelibs4-devel
BuildRequires:   kdebase4-workspace-devel
Provides:        plasma-applet
Requires:        kdebase4-runtime

%description 
Plasmoid that remove the Cashew

%files 
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_ihatethecashew.so
%_kde_datadir/kde4/services/plasma-applet-ihatethecashew.desktop

#-----------------------------------------------------------------------------

%prep
%setup -q -n iHateTheCashew

%build
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}


%clean
rm -rf %buildroot
