from django.shortcuts import render

# Create your views here.
def show_main(request):
    skin_description = [
        {
            'name': 'Elementalist Lux',
            'set': 'Elementalist',
            'tier': 'Ultimate',
            'price': '3250 RP',
        },
        {
            'name': 'Hextech Annie',
            'set': 'Hextech',
            'tier': 'Mythic',
            'price': '10 Hextech Gems',
        },
        {
            'name': "Gentleman Cho'gath",
            'set': 'High Society',
            'tier': 'Legendary',
            'price': '1820 RP',
        },
        {
            'name': 'High Noon Lucian',
            'set': 'High Noon',
            'tier': 'Legendary',
            'price': '1820 RP',
        },
        {
            'name': 'Nightbringer Yasuo',
            'set': 'Nightbringer and Dawnbringer',
            'tier': 'Legendary',
            'price': '1820 RP',
        }
    ]

    context = {
        'application_name': 'League of Legends Skin Collection',
        'name': 'Omar Khalif Muchzi',
        'class': 'Platform-Based Development',
        'skin_description': skin_description
    }

    return render(request, 'main.html', context)