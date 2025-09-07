Vagrant.configure("2") do |config|
  config.vm.box = "net9/ubuntu-24.04-arm64"
  config.vm.hostname = "learning-nginx"

  config.vm.network "public_network", bridge: "en0"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "learning nginx"
    vb.memory = 8192
    vb.cpus = 6
  end

  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.network "forwarded_port", guest: 443, host: 443

  config.vm.synced_folder ".", "/home/vagrant/host"
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt update -y
    sudo apt install -y python3 python3.12-venv python3-pip nodejs npm
  SHELL
end

