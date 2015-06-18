# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	# Base box to build off, and download URL for when it doesn't exist on the user's system already
	config.vm.box = "django-ubuntu-1404-64"
	config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"


	# As an alternative to precise32, VMs can be built from the 'django-base' box as defined at
	# https://github.com/torchbox/vagrant-django-base , which has more of the necessary server config
	# baked in and thus takes less time to initialise. To go down this route, you will need to build
	# and host django-base.box yourself, and substitute your own URL below.
	#config.vm.box = "django-base-v2.1"
	#config.vm.box_url = "http://vmimages.torchbox.com/django-base-v2.1.box"  # Torchbox-internal URL to django-base.box

	# Boot with a GUI so you can see the screen. (Default is headless)
	# config.vm.boot_mode = :gui

	# Assign this VM to a host only network IP, allowing you to access it
	# via the IP.
	# config.vm.network "33.33.33.10"

	#config.vm.provider "virtualbox" do |v|
	#	v.memory = 768
	#	v.cpus = 1
	#end

	# Forward a port from the guest to the host, which allows for outside
	# computers to access the VM, whereas host only networking does not.
	#config v1
	#config.vm.forward_port 8000, 8000
	#config v2
	config.vm.network :forwarded_port, guest: 8000, host: 8000

	# Share an additional folder to the guest VM. The first argument is
	# an identifier, the second is the path on the guest to mount the
	# folder, and the third is the path on the host to the actual folder.
	#config v1
	#config v2
  	config.vm.synced_folder ".", "/home/vagrant/django-waffle"

	# Enable provisioning with a shell script.
	config.vm.provision :shell, :path => "vagrant-conf/install/install.sh", :args => "django-waffle"
end
