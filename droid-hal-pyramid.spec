# These and other macros are documented in dhd/droid-hal-device.inc
%define device pyramid
%define vendor htc
%define vendor_pretty HTC
%define device_pretty Sensation
%define installable_zip 1
%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
