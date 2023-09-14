-- criação do primeiro projeto
create database ecommerce;
use ecommerce;

-- criar tabela cliente

create table clients(
	idCliente int auto_increment primary key,
    Fname varchar(10),
    Minit char(3),
    Lname varchar(20),
    CPF char(11) not null,
    Address varchar(30),
    constraint unique_cpf_client unique(CPF)
);

-- criar tabela produto

create table product(
	idProduct int auto_increment primary key,
    Pname varchar(10),
    classification_kids bool default false,
    category enum('eletronico', 'vestimentas','remedio') not null,
    avaliaçao float default 0,
    size varchar(10),
    constraint unique_cpf_client unique(CPF)
);

-- pagamento
create table payments(
	idclient int,
    id_payment int,
    typePayment enum('Boleto','Cartao'),
    limitAvailable float,
    primary key(idClient, id_payment)
);

-- criar tabela pedido

create table orders(
	idOrder int auto_increment primary key,
    idOrderClient int,
    orderStatus enum('cancelado','confirmado',' Em processo')  default 'Em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    idPaymentCash bool default false,
    constraint fk_ordes_client foreign key (idOrderClient) references clients(idClient)
);

-- criar tabela estoque

create table productStorage(
	idpStorage int auto_increment primary key,
    category enum('cancelado','confirmado',' Em processo')  default 'Em processamento',
    orderDescription varchar(255),
    sendValue float default 10,
    idPaymentCash bool default false,
    constraint fk_ordes_client foreign key (idOrderClient) references clients(idClient)
);