import discord

def create_simple_embed(title: str, description: str, color: discord.Color = discord.Color.blue()) -> discord.Embed:
    """
    Crée un embed Discord simple avec un titre, une description et une couleur.
    
    :param title: Le titre de l'embed.
    :param description: La description de l'embed.
    :param color: La couleur de l'embed (optionnel, par défaut bleu).
    :return: Un objet discord.Embed.
    """
    embed = discord.Embed(title=title, description=description, color=color)
    return embed

def create_advanced_embed(title: str, description: str, fields: list, color: discord.Color = discord.Color.blue()) -> discord.Embed:
    """
    Crée un embed Discord avancé avec un titre, une description, des champs et une couleur.
    
    :param title: Le titre de l'embed.
    :param description: La description de l'embed.
    :param fields: Une liste de tuples (nom, valeur, inline) pour les champs.
    :param color: La couleur de l'embed (optionnel, par défaut bleu).
    :return: Un objet discord.Embed.
    """
    embed = discord.Embed(title=title, description=description, color=color)
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    return embed
