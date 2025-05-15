# 📚 BookStore - Plataforma de Venta de Libros Usados

BookStore es una aplicación web que permite a los usuarios publicar, comprar y vender libros de segunda mano. A diferencia de plataformas tradicionales, BookStore promueve un modelo distribuido de venta entre usuarios.

## ✅ Funcionalidades

- Registro, login y logout de usuarios
- Visualización del catálogo de libros
- Compra de libros con gestión de stock
- Pago simulado
- Envío simulado

## 🚀 Despliegue en AWS

### Objetivo 1 - Despliegue Monolítico
- Aplicación Flask y base de datos MySQL en contenedores Docker
- Servidor EC2 en AWS
- Proxy reverso con NGINX
- Certificado SSL (Let's Encrypt)
- Dominio: `https://www.bookstorejjp.shop`

### Objetivo 2 - Escalamiento Monolito en la Nube
- Auto Scaling Group con EC2s
- Balanceador de carga (AWS ELB)
- Base de datos RDS MySQL
- Sistema de archivos compartido (EFS)

- ![image](https://github.com/user-attachments/assets/792e169b-9f6c-403e-8098-df8b6459aacf)


### Objetivo 3 - Migración a Microservicios
- Microservicio 1: Autenticación
- Microservicio 2: Catálogo
- Microservicio 3: Compra, Pago y Envío
- Despliegue con Kubernetes

## 🧰 Tecnologías

- Flask + Python
- MySQL / Amazon RDS
- Docker + Docker Compose
- NGINX
- Kubernetes
- AWS EC2, ELB, RDS, EFS
- Let's Encrypt (SSL)

## 👥 Integrantes

- Juan Pablo Zuluaga  
- Pedro Saldarriaga  
- Jose Alejandro Duque  

## 📁 Estructura del Proyecto

BookStore/
├── monolith/
├── auth-service/
├── catalog-service/
├── order-service/
├── k8s/
└── README.md
