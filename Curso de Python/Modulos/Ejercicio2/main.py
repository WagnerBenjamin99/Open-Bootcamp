from time import localtime as lt

def main():
    if int(lt().tm_hour) >= 19:
        print('Hora de ir a casa!!')
    else: 
        restante =  (19*60) - ((int(lt().tm_hour)*60) + (int(lt().tm_min)))
        print('Faltan ', restante//60,'horas y', restante%60, 'minutos para ir a casa')
    

if __name__ == "__main__":
    main()