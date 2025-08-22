<?php

/*Através da criação de uma classe que contém características gerais de veículos é possível fazer com que classes menores, 
    por meio de herança, herdem seus atributos sem que eles precisem ser repetidos, assim poupando código e deixando tudo mais rápido */
    
    class Veiculo {
        public $modelo;
        public $cor;
        public $ano;

        public function Andar() {
            echo "Andou";
        }
        public function Parar() {
            echo "Parou";
        }
    }

    class Carro extends Veiculo {
        public $numerodePortas;

        public function AbrirPorta() {
            echo "Porta aberta";
        }
        public function FecharPorta() {
            echo "Porta fechada";
        }

        public function limparParabrisa() {
            echo "Limpando seu parabrisa";
        }
    }

    class Moto extends Veiculo {
        public function darGrau() {
            echo "Dando grau";
        }
    }

    $carro = new Carro();
    $carro -> modelo = "Fusca";
    $carro -> cor = "Branco";
    $carro -> ano = 1998;
    $carro -> numerodePortas = 2;
    $carro -> AbrirPorta();
    echo "<br>";
    var_dump($carro);