# 微体检项目 判断病情代码

# POST json 28项检验数值

# 返回 json n 项病症


class Disease():
    first_order = '00'
    second_order = '00'
    third_order = '00'
    vote = 0

    def __init__(self, code):

        self.first_order = code[:2]
        self.second_order = code[2:4]
        self.third_order = code[4:6]

    def get_code(self):
        return self.first_order + self.second_order + self.third_order

    def set_code(self,fc,sc,tc):
        self.first_order = fc
        self.second_order = sc
        self.third_order = tc

    def add_vote(self, *args):
        if args:
            self.vote += int(args[0])
        else:
            self.vote += 1

    # 有效前缀代码
    def significant_digit(self):
        if not int(self.second_order):
            return self.first_order
        elif not int(self.third_order):
            return self.first_order + self.second_order
        else:
            return self.get_code()
    def copy(self):
        t = Disease(self.get_code())
        t.vote = self.vote
        return t
class DiseaseList():
    diseases = []

    def find_repete(self, pre_code):
        #     寻找有相同前缀的疾病
        for d in self.diseases:
            if d.first_order == pre_code:
                return d
        return None

    def reset(self, del_disease, add_disease):
        #     将重复的病症细化
        del_disease.set_code(add_disease.first_order,add_disease.second_order,add_disease.third_order)
    def add(self, disease):
        #     添加疾病
        old_disease = self.find_repete(disease.first_order)
        if old_disease :
            # 给病症投票
            old_disease.add_vote()
            if len(old_disease.significant_digit())<len(disease.significant_digit()):
                self.reset(old_disease, disease)
            elif old_disease.significant_digit() !=disease.significant_digit() and len(old_disease.significant_digit()) == len(disease.significant_digit()) :
                self.diseases.append(disease)
        else:self.diseases.append(disease)
    
    def adds(self,*args):
        for a in args:
            self.add(a)
    def size(self):
        return len(self.diseases)
    def get_disease(self,index):
        return self.diseases[index]

    def swap(self,sw1,sw2):
        #交换函数
        temp = sw1.copy()
        sw1 = sw2.copy()
        sw2 = temp.copy()
        return sw1,sw2
    def sort_by_vote(self):
        length = self.size()
        for i in range(length):
            for j in range(i+1,length):
                if self.diseases[i].vote<self.diseases[j].vote:
                    self.diseases[i], self.diseases[j] = self.swap(self.diseases[i],self.diseases[j])

    def show_list(self,vote=False):
        if vote == False:
            for i in self.diseases:
                print(i.get_code())
                print(i.get_code())
                print(self)
        else:
            for i in self.diseases:
                print('{0} vote is {1}'.format(i.get_code(),i.vote))
                print('{0} vote is {1}'.format(i.get_code(),i.vote))
                print(self)

if __name__ == '__main__':
    d = Disease('111213')
    c = Disease('111200')
    e = Disease('121300')
    f = Disease('121311')
    k = Disease('121300')
    k1 = Disease('131300')
    k2 = Disease('131311')
    k3 = Disease('131300')
    k4 = Disease('131300')
    l = DiseaseList()
    l.adds(k1, k2, k3, k4)
    l.adds(d,c)
    l.add(e)
    l.add(k)
    l.add(f)
    l.show_list()
    l.sort_by_vote()
    l.show_list(vote=True)
