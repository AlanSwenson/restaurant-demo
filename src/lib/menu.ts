// This will need to be adapted based on your data source
export interface MenuItem {
  name: string;
  description: string;
  price: number;
  category: 'Starters' | 'Mains';
  sort_order: number;
}

export async function getMenuItems(): Promise<MenuItem[]> {
  return [
    {
      name: "Truffle-Infused Wild Mushroom Risotto",
      description: "Arborio rice slowly cooked with porcini and chanterelle mushrooms, finished with black truffle and aged parmesan",
      price: 24,
      category: "Starters",
      sort_order: 1
    },
    {
      name: "Pan-Seared Foie Gras",
      description: "Hudson Valley foie gras with caramelized figs, aged balsamic reduction, and brioche toast",
      price: 32,
      category: "Starters",
      sort_order: 2
    },
    {
      name: "Caviar Service",
      description: "30g of Osetra caviar served with traditional accompaniments and blinis",
      price: 95,
      category: "Starters",
      sort_order: 3
    },
    {
      name: "Lobster Bisque",
      description: "Velvety soup made with Maine lobster, finished with cognac and crème fraîche",
      price: 28,
      category: "Starters",
      sort_order: 4
    },
    {
      name: "Wagyu Beef Carpaccio",
      description: "Thinly sliced A5 wagyu with shaved black truffle, aged parmesan, and extra virgin olive oil",
      price: 34,
      category: "Starters",
      sort_order: 5
    },
    {
      name: "Seared Sea Scallops",
      description: "Diver scallops with cauliflower purée, golden raisins, and brown butter sauce",
      price: 26,
      category: "Starters",
      sort_order: 6
    },
    {
      name: "Dry-Aged Prime Ribeye",
      description: "45-day aged 16oz ribeye, bone marrow butter, roasted wild mushrooms, and truffle potato purée",
      price: 85,
      category: "Mains",
      sort_order: 1
    },
    {
      name: "Butter-Poached Maine Lobster",
      description: "Whole 2lb lobster with saffron risotto, asparagus, and vanilla-infused lobster sauce",
      price: 95,
      category: "Mains",
      sort_order: 2
    },
    {
      name: "Duck Breast à l'Orange",
      description: "Muscovy duck breast, citrus-cognac sauce, confit leg, and roasted heritage carrots",
      price: 68,
      category: "Mains",
      sort_order: 3
    },
    {
      name: "Chilean Sea Bass",
      description: "Miso-glazed sea bass with forbidden rice, baby bok choy, and ginger-lemongrass broth",
      price: 72,
      category: "Mains",
      sort_order: 4
    },
    {
      name: "Rack of Colorado Lamb",
      description: "Herb-crusted lamb, roasted garlic polenta, baby vegetables, and rosemary jus",
      price: 78,
      category: "Mains",
      sort_order: 5
    },
    {
      name: "Black Truffle Tagliatelle",
      description: "House-made pasta, shaved black truffles, aged parmesan, and brown butter sauce",
      price: 65,
      category: "Mains",
      sort_order: 6
    }
  ];
} 