from scripts.load_data import get_data
from scripts.analyze import calculate_markups
from scripts.generate_graphs import save_bar_chart

def main():
    df = get_data()
    df, top_10 = calculate_markups(df)
    save_bar_chart(top_10)
    
    print("Analysis complete!")
    print("\nTop 5 Highest Markup States:")
    print(top_10.head(5).round(1).astype(str) + "%")
    print("\nChart saved to: graphs/top_10_markup_states.png")

if __name__ == "__main__":
    main()
