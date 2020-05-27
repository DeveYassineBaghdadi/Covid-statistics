import requests
import json
import datetime
import smtplib
import getpass
import time

import yagmail

COUNTRIES = ['Afghanistan', 'Albania', 'Algeria', 'Andorra',
             'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina',
             'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
             'Bosnia and Herzegovina', 'Botswana', 'Brazil',
             'British Virgin Islands', 'Brunei', 'Bulgaria',
             'Burkina Faso', 'Burundi', 'CAR', 'Cabo Verde',
             'Cambodia', 'Cameroon', 'Canada', 'Caribbean Netherlands',
             'Cayman Islands', 'Chad', 'Channel Islands', 'Chile',
             'China', 'Colombia', 'Congo', 'Costa Rica', 'Croatia',
             'Cuba', 'Curaçao', 'Cyprus', 'Czechia', 'DRC', 'Denmark',
             'Diamond Princess', 'Djibouti', 'Dominica', 'Dominican Republic',
             'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
             'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe Islands',
             'Falkland Islands', 'Fiji', 'Finland', 'France', 'French Guiana',
             'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
             'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala',
             'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong',
             'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
             'Isle of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan',
             'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
             'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
             'MS Zaandam', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
             'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte',
             'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat',
             'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands',
             'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
             'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palestine',
             'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
             'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
             'Réunion', 'S. Korea', 'Saint Kitts and Nevis', 'Saint Lucia',
             'Saint Martin', 'Saint Pierre Miquelon', 'San Marino',
             'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
             'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten',
             'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Sudan',
             'Spain', 'Sri Lanka', 'St. Barth', 'St. Vincent Grenadines',
             'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
             'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Trinidad and Tobago',
             'Tunisia', 'Turkey', 'Turks and Caicos', 'UAE', 'UK', 'USA', 'Uganda',
             'Ukraine', 'Uruguay', 'Uzbekistan', 'Vatican City', 'Venezuela',
             'Vietnam', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']




class Main:
    def __init__(self):
        pass

    def get_world_statistics(self):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"

        headers = {
            'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
            'x-rapidapi-key': "8598529df9mshf9c27948c4cf81dp150776jsn6423b91f24f4"
        }

        response = requests.request("GET", url, headers=headers)
        # print(json.loads(response.text)['total_cases'])
        return json.loads(response.text)

    def get_world_statistics_by_contries(self):
        url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"

        headers = {
            'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
            'x-rapidapi-key': "8598529df9mshf9c27948c4cf81dp150776jsn6423b91f24f4"
        }

        response = requests.request("GET", url, headers=headers)

        return json.loads(response.text)

    def send_mail(self, yag, body):

        with open('mail.txt', 'r') as f:
            sendTo = [i.replace('\n', '') for i in f.readlines()]


        sub = 'Some new statistics of CoronaVirus'
        # msg = f'subject: {sub},\n\n{body}'


        # with smtplib.SMTP('smtp.gmail.com', 587) as snd:
        #     snd.ehlo()
        #     snd.starttls()
        #     snd.ehlo()
        #     # enable less secure apps option from :
        #     # https://myaccount.google.com/lesssecureapps
        #     # https://www.google.com/settings/security/lesssecureapps
        #     snd.login(sender, password)
        #
        #     for i in sendTo:
        #         try:
        #             snd.sendmail(sender, i, msg)
        #             print(i, ' is done ')
        #         except Exception as e:
        #             print(' not sent to ', i)


        for mailAdd in sendTo:
            yag.send(mailAdd, sub, body)
            print(f'sending to : {mailAdd} .. DONE ')


if __name__ == '__main__':

    m = Main()
    update_date = '0'
    morocco_cases = '0'
    morocco_deaths = '0'
    morocco_recovered = '0'
    morocco_new_cases = '0'
    morocco_new_deaths = '0'
    morocco_new_recovered = '0'



    #{'total_cases': '2,073,555', 'total_deaths': '134,020', 'total_recovered': '509,041', 'new_cases': '75,695', 'new_deaths': '7,420', 'statistic_taken_at': '2020-04-15 21:51:09'}

    sender = 'email.adress@gmail.com'
    password = 'password'
    yag = yagmail.SMTP(sender, password)

    while True:
        ########### for Morocco ############à
        nM_cases = ''
        morocco_data = m.get_world_statistics_by_contries()
        world_data = m.get_world_statistics()
        world_cases = world_data['total_cases']

        for d in morocco_data['countries_stat']:
            if d['country_name'] == 'Morocco':
                #{'country_name': 'Morocco', 'cases': '2,024', 'deaths': '127', 'region': '', 'total_recovered': '229', 'new_deaths': '1', 'new_cases': '136', 'serious_critical': '1', 'active_cases': '1,668', 'total_cases_per_1m_population': '55'}
                nM_cases = d['cases']
                morocco_deaths = d['deaths']
                morocco_new_cases = d['new_cases']
                morocco_new_deaths = d['new_deaths']

                if morocco_recovered != d['total_recovered']:
                    morocco_new_recovered = int(str(d['total_recovered']).replace(',', '')) - int(str(morocco_recovered).replace(',', ''))
                    morocco_recovered = d['total_recovered']

        if morocco_cases != nM_cases:#send the email
            # morocco_new_recovered = int(str(nM_cases).replace(',', '')) - int(str(morocco_cases).replace(',', ''))
            update_date = morocco_data['statistic_taken_at']
            morocco_cases = nM_cases
            msg = f"""
                <h3 style="text-align: center;">The latest update of coronavirus cases statistics in MOROCCO</h3>
                <p>This is an online <a href="https://github.com/DeveYassineBaghdadi/Covid-statistics">script</a> created by <strong><a href="https://deveyassinebaghdadi.github.io">yassine baghdadi </a></strong> to keep you up to date (24h/24h).<br /> If you want an customized mail setting all you've to do is just text me. via : <a href="https://api.whatsapp.com/send?phone=+212630504606"> whatsapp </a><a> or </a><a href="https://web.facebook.com/yassine.baghdadi.391">facebook</a><a> or </a><a href="https://www.linkedin.com/in/yassine-baghdadi-687064182/">linkedin</a><a>, </a><a href="https://www.instagram.com/yassine__baghdadi/">instagram </a><a>.</a></p>
                <p>Updated on : {update_date}.</p>
                <p style="text-align: center;"><strong>new cases in morocco&nbsp;</strong></p>
                <strong>Total cases : </strong>{morocco_cases} <span style="color: #008000;">+{morocco_new_cases} </span> ({round((int(str(morocco_cases).replace(',', ''))/int(str(world_cases).replace(',', '')))*100, 2)}% of the world cases ).<br>
                <strong>Total&nbsp;Recovered</strong> :{morocco_recovered}&nbsp;<span style="color: #008000;">+{morocco_new_recovered}</span>&nbsp;({round((int(str(morocco_recovered).replace(',', ''))/int(str(morocco_cases).replace(',', '')))*100, 2)}%).<br>
                <strong>Total deaths</strong> : {morocco_deaths}&nbsp;<span style="color: #ff0000;">+{morocco_new_deaths}</span>&nbsp;({round((int(str(morocco_deaths).replace(',', ''))/int(str(morocco_cases).replace(',', '')))*100, 2)}%).<br>
                sent by&nbsp;<a href="https://deveyassinebaghdadi.github.io">Yassine Baghdadi</a>.<br>
                links :
                <ul>
                    <li><a href="https://github.com/DeveYassineBaghdadi">Github</a></li>
                    <li><a href="https://github.com/DeveYassineBaghdadi/Covid-statistics">Source Code</a></li>
                    <li><a href="https://www.linkedin.com/in/yassine-baghdadi-687064182/">LinkedIn</a></li>
                    <li><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=BLS73NBQEJ89N&amp;source=url">Donation</a></li>
                </ul>
            """
            m.send_mail(yag, msg)

        ############ for whole world ################
        if str(time.strftime("%H:%M", time.gmtime())) == '22:00':
            world_data = m.get_world_statistics()
            updated_date = world_data['statistic_taken_at']
            world_cases = world_data['total_cases']
            world_deaths = world_data['total_deaths']
            world_recovered = world_data['total_recovered']
            world_new_cases = world_data['new_cases']
            world_new_deaths = world_data['new_deaths']
            data_by_countries = m.get_world_statistics_by_contries()
            updated_date = data_by_countries['statistic_taken_at']
            cases_by_countries_html = ''

            for c in data_by_countries['countries_stat']:
                if c['country_name']:
                    print(c)
                    cases_by_countries_html += f"""<tr><td style="width: 166px; text-align: center;">{c["country_name"]}</td><td style="width: 166px; text-align: center;">{c["cases"]}<span style="color: #008000;">+{c["new_cases"]}</span></td><td style="width: 166px; text-align: center;">{c["total_recovered"]}</td><td style="width: 166px; text-align: center;">{c["deaths"]}<span style="color: #ff0000;">+{c["new_deaths"]}</span></td><td style="width: 166px; text-align: center;">{c["active_cases"]}</td></tr>"""

            msg = f"""
                            <h3 style="text-align: center;">The latest update of coronavirus cases statistics in The World</h3>
                            <p>This is an online <a href="https://github.com/DeveYassineBaghdadi/Covid-statistics">script</a> created by <strong><a href="https://deveyassinebaghdadi.github.io">yassine baghdadi </a></strong> to keep you up to date (24h/24h).<br> If you want an customized setting all you've to do is just text me. via : <a href="https://api.whatsapp.com/send?phone=+212630504606"> whatsapp </a><a> or </a><a href="https://web.facebook.com/yassine.baghdadi.391">facebook</a><a> or </a><a href="https://www.linkedin.com/in/yassine-baghdadi-687064182/">linkedin</a><a>, </a><a href="https://www.instagram.com/yassine__baghdadi/">instagram </a><a>.</a></p>
                            <p>Updated on : {updated_date}.</p>
                            <p style="text-align: center;"><strong>New Cases in The World&nbsp;</strong></p>
                            <p><strong>Total cases : </strong>{world_cases} <span style="color: #008000;">+{world_new_cases}</span>&nbsp;.<br>
                            <strong>Total&nbsp;Recovered</strong> :{world_recovered}&nbsp;({round((int(str(world_recovered).replace(',', '')) / int(str(world_cases).replace(',', ''))) * 100, 2)}%).<br>
                            <strong>Total deaths</strong> : {world_deaths}&nbsp;<span style="color: #ff0000;">+{world_new_deaths}</span>&nbsp;({round((int(str(world_deaths).replace(',', '')) / int(str(world_cases).replace(',', ''))) * 100, 2)}%).</p><br>
                            <table  style=" width: 573px; margin-left: auto; margin-right: auto;" border="2px"><tr><td style="width: 166px; text-align: center;"><strong>Country</strong></td><td style="width: 88px; text-align: center;"><strong>Cases</strong></td><td style="width: 90px; text-align: center;"><strong>Recovered</strong></td><td style="width: 84px; text-align: center;"><strong>Deaths</strong></td><td style="width: 111px; text-align: center;"><strong>Active_Cases</strong></td></tr>{cases_by_countries_html}

                            </table>
                            <p>sent by&nbsp;<a href="https://deveyassinebaghdadi.github.io">Yassine Baghdadi</a>.<br> links:&nbsp;</p>
                            <ul>
                                    <li><a href="https://github.com/DeveYassineBaghdadi">Github</a></li>
                                    <li><a href="https://github.com/DeveYassineBaghdadi/Covid-statistics">Source Code</a></li>
                                    <li><a href="https://www.linkedin.com/in/yassine-baghdadi-687064182/">LinkedIn</a></li>
                                    <li><a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=BLS73NBQEJ89N&amp;source=url">Donation</a></li>
                            </ul>

                    """

            m.send_mail(yag, msg)





