# -*- mode: ruby -*-
# # vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox"
  config.vm.box = "ubuntu/disco64"
  config.vm.provider :virtualbox do |vb|
    vb.gui    = true
    vb.memory = 2048

    # https://askubuntu.com/questions/897701/official-ubuntu-16-04-vagrant-cloud-image-boots-very-slowly
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ] # THIS LINE
  end
  config.vm.synced_folder ".", "/home/vagrant/i3-config"


  # Install the whole thing
  config.vm.provision "shell", inline: "sudo -Hu vagrant /home/vagrant/i3-config/bootstrap"
end
