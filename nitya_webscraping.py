from bs4 import BeautifulSoup
import requests
import warnings
import re
import os.path

def scrape():
    MAX_DEPTH = 1
    SAVE_DIR = './websitetexts/'

    all_websites = [[['https://www.visitpittsburgh.com/', 0]],
                    [['https://pittsburghpa.gov/finance/tax-forms', 0]],
                    [['https://pittsburghopera.org/', 0]],
                    [['https://trustarts.org/', 0]],
                    [['https://carnegiemuseums.org/', 0]],
                    [['https://www.heinzhistorycenter.org/', 0]],
                    [['https://www.thefrickpittsburgh.org/', 0]],
                    [['https://bananasplitfest.com/', 0]],
                    [['https://www.visitpittsburgh.com/things-to-do/pittsburgh-sports-teams/', 0]],
                    [['https://www.mlb.com/pirates', 0]],
                    [['https://www.steelers.com/', 0]],
                    [['https://www.nhl.com/penguins/', 0]]]

    roots = ['visitpittsburgh.com',
             'pittsburghpa.gov',
             'pittsburghopera.org',
             'trustarts.org',
             'carnegiemuseums.org',
             'heinzhistorycenter.org',
             'thefrickpittsburgh.org',
             'bananasplitfest.com',
             'visitpittsburgh.com',
             'mlb.com',
             'steelers.com',
             'nhl.com']

    j = 0
    for i in range(len(all_websites)):
        while len(all_websites[i]) > 0:
            try:
                page = requests.get(all_websites[i][0][0], verify=False)
                soup = BeautifulSoup(page.text, "html.parser")
                paras = []
                filedir = SAVE_DIR + '_'.join(re.split('[/.\-?=&*+%]', all_websites[i][0][0][12:-1]))[:200] + '.txt'
                if not os.path.isfile(filedir):
                    for _ in soup.find_all('p'):
                        text = _.get_text().lstrip()
                        if len(text.split()) > 10:
                            paras.append(text)

                    with open(filedir, "w", encoding="utf-8") as text_file:
                        text_file.writelines('\n'.join(paras))
                        text_file.close()

                j += 1
                print(f'Done website {i+1}, {j}: {all_websites[i][0][0]}')

                if all_websites[i][0][1]+1 <= MAX_DEPTH:
                    for _ in soup.find_all('a', href=True):
                        link = f"{'/'.join(all_websites[i][0][0].split('/')[:-1])}{_['href']}"if _['href'][0] == '/' else _['href']
                        # print(link)
                        if (((link not in [all_websites[i][_][0] for _ in range(len(all_websites[i]))])
                                and ('http' in link))
                                and (roots[i] in link)):
                            all_websites[i].append([link, all_websites[i][0][1]+1])
                all_websites[i].pop(0)
            except requests.exceptions.SSLError:
                print("SSL Exception Occurred!")
                all_websites[i].pop(0)
            except requests.exceptions.ConnectionError:
                print("Connection Error!")
                all_websites[i].pop(0)
            except AssertionError:
                print("Assertion Error!")
                all_websites[i].pop(0)
            except Exception:
                print("General Error!")
                all_websites[i].pop(0)
if __name__ == '__main__':
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        scrape()