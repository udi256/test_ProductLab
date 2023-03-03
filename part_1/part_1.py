import networkx as nx


def check_relation(net, first, second):
    try:
        return True if nx.dijkstra_path_length(g,first,second) else False

    except nx.exception.NetworkXNoPath:
        return False
    

def generete_network(net):
    g = nx.Graph()
    for connect in net:
        g.add_nodes_from(connect)

    g.add_edges_from(net)
    return g

def main():
    net = (
    ("Ваня", "Лёша"), ("Лёша", "Катя"),
    ("Ваня", "Катя"), ("Вова", "Катя"),
    ("Лёша", "Лена"), ("Оля", "Петя"),
    ("Стёпа", "Оля"), ("Оля", "Настя"),
    ("Настя", "Дима"), ("Дима", "Маша")
    )
    global g #объявлено глобальной т.к. необходимо использовать в функции список параметрой которой определен условием
    # задачи. и вынесено из функции для однократной генерации и дальнейшего переиспользования
    g = generete_network(net)

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True

if __name__ == '__main__':
    main()