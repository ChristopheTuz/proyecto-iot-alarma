using System.Text;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System.Diagnostics;

namespace Send{
    class Program{
        static void Main(string[] args){
            var factory = new ConnectionFactory { HostName = "localhost" };
            string scriptPath = "../alarma.py";

            using(IConnection connection = factory.CreateConnection()){ // Aquí se crea la conexión.
                using(var channel = connection.CreateModel()){ // Aquí se crea el canal.

                    channel.QueueDeclare(queue: "hello", durable: false, exclusive: false, autoDelete: false, arguments: null); // Se crea la cola.
        
                    var consumer = new EventingBasicConsumer(channel);

                    consumer.Received += (model, ea) => {
                        var body = ea.Body.ToArray();
                        var message = Encoding.UTF8.GetString(body);
                        
                        if(message != ""){
                            //Console.WriteLine($"[x] Receive: {message}");
                            
                            if(message == "1"){
                                Console.WriteLine("[O] Alarma desactivada");
                                Process.Start("python", scriptPath);
                            }else{
                                Console.WriteLine("[O] Alarma activada");
                                Process.Start("python", scriptPath);
                            }
                            
                        }else{
                            Console.WriteLine("[X] Error: Usuario no valido");
                        }
                    };
                    
                    channel.BasicConsume(queue: "hello", autoAck: true, consumer:consumer);

                    Console.WriteLine("Listening...");
                    Console.WriteLine("Press any key to exit: ");
                    Console.ReadLine();

                }
            }
        } //Main
    } //Class
} //Send