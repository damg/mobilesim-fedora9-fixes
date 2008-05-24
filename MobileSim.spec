Summary: MobileSim, a robot simulator
Name:MobileSim
Version: 0.4.0
Release: 1
Source0: %{name}-src-%{version}.tgz
Patch0: mobilesim-fixed-headers-and-makefile-0.4.0.patch
License: GPL
Group: Development/Tools
Requires: gtk2
BuildRoot: %{_builddir}/%{name}-src-%{version}/
%description
MobileSim is a program simulating a robot in an environment. 
It is to be used in combination with the ARIA library.

%changelog
* Sat May 24 2008 Dmitri Bachtin <damg.dev@gmail.com>
- Initial build.

%prep
export MOBILESIM_RELEASE=1
%setup -n %{name}-src-%{version}
%patch -p1

%build
make

%install
export RPM_BUILD_ROOT2="$RPM_BUILD_ROOT"2
cp -rf $RPM_BUILD_ROOT $RPM_BUILD_ROOT2
cd $RPM_BUILD_ROOT2
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/local/MobileSim \
		$RPM_BUILD_ROOT/usr/local/MobileSim \
		$RPM_BUILD_ROOT/usr/local/MobileSim \
		$RPM_BUILD_ROOT/usr/share/applications \
		$RPM_BUILD_ROOT/usr/local/bin \
		$RPM_BUILD_ROOT/usr/local/MobileSim
install -s -m 755 $RPM_BUILD_ROOT2/MobileSim $RPM_BUILD_ROOT/usr/local/MobileSim/MobileSim
install -m 644 $RPM_BUILD_ROOT2/config/icon.png $RPM_BUILD_ROOT/usr/local/MobileSim/icon.png
install -m 644 $RPM_BUILD_ROOT2/config/columbia-OL.map $RPM_BUILD_ROOT/usr/local/MobileSim/columbia-OL.map
install -m 644 $RPM_BUILD_ROOT2/config/AMROffice.map $RPM_BUILD_ROOT/usr/local/MobileSim/AMROffice.map
install -m 644 $RPM_BUILD_ROOT2/config/AMROffice.world $RPM_BUILD_ROOT/usr/local/MobileSim/AMROffice.world
install -m 644 $RPM_BUILD_ROOT2/config/AMROffice.map.inc $RPM_BUILD_ROOT/usr/local/MobileSim/AMROffice.map.inc
install -m 644 $RPM_BUILD_ROOT2/config/PioneerRobotModels.world.inc $RPM_BUILD_ROOT/usr/local/MobileSim/PioneerRobotModels.world.inc
install -m 644 $RPM_BUILD_ROOT2/config/MobileSim.desktop $RPM_BUILD_ROOT/usr/share/applications/MobileSim.desktop
install -m 644 $RPM_BUILD_ROOT2/README.html $RPM_BUILD_ROOT/usr/local/MobileSim/README.html
install -m 644 $RPM_BUILD_ROOT2/screenshot.png $RPM_BUILD_ROOT/usr/local/MobileSim/README.html
install -m 644 $RPM_BUILD_ROOT2/Changes.txt $RPM_BUILD_ROOT/usr/local/MobileSim/Changes.txt
install -m 644 $RPM_BUILD_ROOT2/COPYING $RPM_BUILD_ROOT/usr/local/MobileSim/COPYING
install -m 644 $RPM_BUILD_ROOT2/version.txt $RPM_BUILD_ROOT/usr/local/MobileSim/version.txt
cd $RPM_BUILD_ROOT/usr/local/bin
ln -s -f ../MobileSim/MobileSim MobileSim
rm -rf $RPM_BUILDROOT2
%files
%defattr(-,root,root)
/usr/local/MobileSim/MobileSim
/usr/local/MobileSim/AMROffice.map
/usr/local/MobileSim/README.html
/usr/local/MobileSim/columbia-OL.map
/usr/local/MobileSim/AMROffice.map.inc
/usr/local/MobileSim/icon.png
/usr/local/MobileSim/Changes.txt
/usr/local/MobileSim/PioneerRobotModels.world.inc
/usr/local/MobileSim/AMROffice.world
/usr/local/MobileSim/version.txt
/usr/local/MobileSim/COPYING
/usr/local/bin/MobileSim
/usr/share/applications/MobileSim.desktop
/debugfiles.list
/debuglinks.list
/debugsources.list

