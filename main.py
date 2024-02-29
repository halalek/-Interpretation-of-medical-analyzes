from experta import *


class Diabetes(Fact):  # مرض السكري
    pass


class Hormones(Fact):  # امراض الغدد
    pass


class BoneDiseases(Fact):  # امراض العظام
    pass


class BloodTests(Fact):  # تحاليل دموية
    pass


class DetectionAnalysis(KnowledgeEngine):
    @Rule(Fact(start="yes"))
    def action1(self):
        print("1- Diabates Analysis ...")
        print("2- Bone Analysis ...")
        print("3- Blood Analysis ...")
        print("4- Hormones Analysis ...")
        choose = input("Enter your Choose :")
        self.declare(Fact(choose=int(choose)))
        pass

    @Rule(Fact(choose=1))
    def action2(self):
        Ph = input("Enter rate of PH :")
        PaO2 = input("Enter rate of PaO2 :")
        HCO3 = input("Enter rate of HCO3 :")
        PCO2 = input("Enter rate of PCO2 :")
        self.declare(Diabetes(Ph=float(Ph)), Diabetes(PaO2=int(PaO2)), Diabetes(HCO3=int(HCO3)),
                     Diabetes(PCO2=int(PCO2)))
        pass

    @Rule(AND(Diabetes(Ph=P(lambda Ph: Ph >= 0.18) & P(lambda Ph: Ph <= 0.48)),
              Diabetes(PaO2=P(lambda PaO2: PaO2 >= 80) & P(lambda PaO2: PaO2 <= 100)),
              Diabetes(HCO3=P(lambda HCO3: HCO3 >= 22) & P(lambda HCO3: HCO3 <= 28)),
              Diabetes(PCO2=P(lambda PCO2: PCO2 >= 35) & P(lambda PCO2: PCO2 <= 45))))
    def action3(self):
        r="You are not suffer from Diabetes"
        file=open("result.txt","a")
        file.write(r+'\n')
        print("You are not suffer from Diabetes ...")
        pass

    @Rule(OR(Diabetes(Ph=P(lambda Ph: Ph < 0.18) | P(lambda Ph: Ph > 0.48)),
             Diabetes(PaO2=P(lambda PaO2: PaO2 < 80) | P(lambda PaO2: PaO2 > 100)),
             Diabetes(HCO3=P(lambda HCO3: HCO3 < 22) | P(lambda HCO3: HCO3 > 28)),
             Diabetes(PCO2=P(lambda PCO2: PCO2 < 35) | P(lambda PCO2: PCO2 > 45))))
    def action4(self):
        # print("You are suffer from Diabetes ...")
        pass

    @Rule(Diabetes(Ph=P(lambda Ph: Ph < 0.18)))
    def action5(self):
        r = "your PH rate is low"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your PH rate is low ...")
        pass

    @Rule(Diabetes(Ph=P(lambda Ph: Ph > 0.48)))
    def action6(self):
        r = "your PH rate is high"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your PH rate is high ...")
        pass

    @Rule(Diabetes(PaO2=P(lambda PaO2: PaO2 < 80)))
    def action7(self):
        r = "your PaO2 rate is low"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your PaO2 rate is low ...")
        pass

    @Rule(Diabetes(PaO2=P(lambda PaO2: PaO2 > 100)))
    def action8(self):
        r = "your PaO2 rate is high"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your PaO2 rate is high ...")
        pass

    @Rule(Diabetes(HCO3=P(lambda HCO3: HCO3 < 22)))
    def action9(self):
        r = "your HCO3 rate is low"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your HCO3 rate is low ...")
        pass

    @Rule(Diabetes(HCO3=P(lambda HCO3: HCO3 > 28)))
    def action10(self):
        r = "your HCO3 rate is high"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your HCO3 rate is high ...")
        pass

    @Rule(Diabetes(PCO2=P(lambda PCO2: PCO2 < 35)))
    def action11(self):
        r = "your PCO2 rate is low"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your PCO2 rate is low ...")
        pass

    @Rule(Diabetes(PCO2=P(lambda PCO2: PCO2 > 45)))
    def action12(self):
        r = "your PCO2 rate is high"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("your PCO2 rate is high ...")
        pass

    @Rule(Fact(choose=3))
    def action13(self):
        print("1- Female")
        print("2- Male")
        type = input("Enter your Choose :")
        self.declare(BloodTests(type=type))
        pass

    @Rule(BloodTests(type="Female"))
    def action14(self):
        Hemoglobin = input("Enter rate of Hemoglobin :")
        Platelets = input("Enter rate of Platelets :")
        Leukocyte = input("Enter rate of Leukocyte :")
        self.declare(BloodTests(HemoglobinF=int(Hemoglobin)), BloodTests(Platelets=int(Platelets)),
                     BloodTests(Leukocyte=int(Leukocyte)))
        pass

    @Rule(AND(BloodTests(HemoglobinF=P(lambda HemoglobinF: HemoglobinF >= 12) & P(lambda HemoglobinF: HemoglobinF <= 16)),
              BloodTests(Platelets=P(lambda Platelets: Platelets >= 150000) & P(lambda Platelets: Platelets <= 450000)),
              BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte >= 4500) & P(lambda Leukocyte: Leukocyte <= 10500))))
    def action15(self):
        r = "Your Blood test is very Normal"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Your Blood test is very Normal ...")
        pass

    @Rule(BloodTests(type="Male"))
    def action16(self):
        Hemoglobin = input("Enter rate of Hemoglobin :")
        Platelets = input("Enter rate of Platelets :")
        Leukocyte = input("Enter rate of Leukocyte :")
        self.declare(BloodTests(HemoglobinM=int(Hemoglobin)), BloodTests(Platelets=int(Platelets)),
                     BloodTests(Leukocyte=int(Leukocyte)))
        pass

    @Rule(
        AND(BloodTests(HemoglobinM=P(lambda HemoglobinM: HemoglobinM >= 12) & P(lambda HemoglobinM: HemoglobinM <= 16)),
            BloodTests(Platelets=P(lambda Platelets: Platelets >= 150000) & P(lambda Platelets: Platelets <= 450000)),
            BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte >= 4500) & P(lambda Leukocyte: Leukocyte <= 10500))))
    def action17(self):
        r = "Your Blood test is very Normal"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Your Blood test is very Normal ...")
        pass

    @Rule(OR(BloodTests(HemoglobinF=P(lambda HemoglobinF: HemoglobinF < 12) | P(lambda HemoglobinF: HemoglobinF > 16)),
             BloodTests(Platelets=P(lambda Platelets: Platelets < 150000) | P(lambda Platelets: Platelets > 450000)),
             BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte < 4500) | P(lambda Leukocyte: Leukocyte > 10500))))
    def action18(self):
        # print("Your Blood test is not Normal ...")
        pass

    @Rule(OR(BloodTests(HemoglobinM=P(lambda HemoglobinM: HemoglobinM < 13) | P(lambda HemoglobinM: HemoglobinM > 18)),
             BloodTests(Platelets=P(lambda Platelets: Platelets < 150000) | P(lambda Platelets: Platelets > 450000)),
             BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte < 4500) | P(lambda Leukocyte: Leukocyte > 10500))))
    def action17(self):
        # print("Your Blood test is not Normal ...")
        pass

    @Rule(BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte > 10500) & P(lambda Leukocyte: Leukocyte < 20000)))
    def action18(self):
        r = "High Leukocyte level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High Leukocyte level ...")
        pass

    @Rule(BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte > 20000) & P(lambda Leukocyte: Leukocyte < 25000)))
    def action19(self):
        r = "You may have a Viral or Bacterial Infection"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("You may have a Viral or Bacterial Infection ...")
        pass

    @Rule(BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte >= 25000)))
    def action20(self):
        r = "You may have a Cancer Tumor"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("You may have a Cancer Tumor ...")
        pass

    @Rule(BloodTests(Leukocyte=P(lambda Leukocyte: Leukocyte < 4500)))
    def action21(self):
        r = "Low Leukocyte level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low Leukocyte level ...")
        pass

    @Rule(BloodTests(Platelets=P(lambda Platelets: Platelets < 150000)))
    def action22(self):
        r = "You may have Bone Marrow Tumor , an Immune disease or Cancer"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("You may have Bone Marrow Tumor , an Immune disease or Cancer ...")
        pass

    @Rule(BloodTests(Platelets=P(lambda Platelets: Platelets > 450000)))
    def action23(self):
        r = "High Platelets level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High Platelets level ...")
        pass

    @Rule(BloodTests(HemoglobinM=P(lambda HemoglobinM: HemoglobinM < 13)))
    def action24(self):
        r = "Low Hemoglobin level and this causes Anemia"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low Hemoglobin level and this causes Anemia ...")
        pass

    @Rule(BloodTests(HemoglobinF=P(lambda HemoglobinF: HemoglobinF < 12)))
    def action25(self):
        r = "Low Hemoglobin level and this causes Anemia"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low Hemoglobin level and this causes Anemia ...")
        pass

    @Rule(BloodTests(HemoglobinM=P(lambda HemoglobinM: HemoglobinM > 18)))
    def action26(self):
        r = "High Hemoglobin level and this causes Fatigue and Pallid"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High Hemoglobin level and this causes Fatigue and Pallid ...")
        pass

    @Rule(BloodTests(HemoglobinF=P(lambda HemoglobinF: HemoglobinF > 16)))
    def action27(self):
        r = "High Hemoglobin level and this causes Fatigue and Pallid"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High Hemoglobin level and this causes Fatigue and Pallid ...")
        pass

    @Rule(Fact(choose=2))
    def action28(self):
        VitD = input("Enter rate of Vitamin D :")
        Caly = input("Enter rate of Calcitonin :")
        Pth = input("Enter rate of PTH :")
        self.declare(BoneDiseases(VitD=int(VitD)), BoneDiseases(Caly=int(Caly)), BoneDiseases(Pth=int(Pth)))
        pass

    @Rule(AND(BoneDiseases(VitD=P(lambda VitD: VitD >= 20) & P(lambda VitD: VitD <= 40)),
              BoneDiseases(Caly=P(lambda Caly: Caly <= 10)),
              BoneDiseases(Pth=P(lambda Pth: Pth >= 14) & P(lambda Pth: Pth <= 65))))
    def action29(self):
        r = "You do not suffer from Bone Diseases"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("You do not suffer from Bone Diseases ...")
        pass

    @Rule(OR(BoneDiseases(VitD=P(lambda VitD: VitD < 20) | P(lambda VitD: VitD > 40)),
             BoneDiseases(Caly=P(lambda Caly: Caly > 10)),
             BoneDiseases(Pth=P(lambda Pth: Pth < 14) | P(lambda Pth: Pth > 65))))
    def action30(self):
        # print("You have Bone Disease ...")
        pass

    @Rule(BoneDiseases(VitD=P(lambda VitD: VitD < 20)))
    def action31(self):
        r = "Low Vitamin D level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low Vitamin D level ...")
        pass

    @Rule(BoneDiseases(VitD=P(lambda VitD: VitD > 40)))
    def action32(self):
        r = "High Vitamin D level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High Vitamin D level ...")
        pass

    @Rule(BoneDiseases(Caly=P(lambda Caly: Caly > 10)))
    def action33(self):
        r = "High Calcitonin level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High Calcitonin level ...")
        pass

    @Rule(BoneDiseases(Pth=P(lambda Pth: Pth < 14)))
    def action34(self):
        r = "Low PTH level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low PTH level ...")
        pass

    @Rule(BoneDiseases(Pth=P(lambda Pth: Pth > 65)))
    def action35(self):
        r = "High PTH level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High PTH level ...")
        pass

    @Rule(Fact(choose=4))
    def action36(self):
        print("1- Female")
        print("2- Male")
        print("3- Children")
        type = input("Enter your Choose :")
        self.declare(Hormones(type=type))
        pass

    @Rule(Hormones(type="Female"))
    def action37(self):
        IGF = input("Enter rate of IGF :")
        FT4 = input("Enter rate of FT4 :")
        ADH = input("Enter rate of ADH :")
        TSH = input("Enter rate of TSH :")
        PRL = input("Enter rate of PRL :")
        KLS = input("Enter rate of KLS :")

        self.declare(Hormones(IGFf=float(IGF)), Hormones(FT4=float(FT4)),
                     Hormones(ADH=float(ADH)), Hormones(TSH=float(TSH)), Hormones(PRL=float(PRL)),
                     Hormones(KLS=float(KLS)))
        pass

    @Rule(AND(Hormones(IGFf=P(lambda IGFf: IGFf >= 10) & P(lambda IGFf: IGFf <= 14)),
              Hormones(FT4=P(lambda FT4: FT4 >= 0.7) & P(lambda FT4: FT4 <= 1.9)),
              Hormones(ADH=P(lambda ADH: ADH >= 0.4) & P(lambda ADH: ADH <= 7)),
              Hormones(TSH=P(lambda TSH: TSH >= 0.5) & P(lambda TSH: TSH <= 5)),
              Hormones(PRL=P(lambda PRL: PRL >= 80) & P(lambda PRL: PRL <= 400)),
              Hormones(KLS=P(lambda KLS: KLS >= 10) & P(lambda KLS: KLS <= 20))))
    def action38(self):
        r = "Your Hormones test is very Normal"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Your Hormones test is very Normal ...")
        pass

    @Rule(Hormones(type="Male"))
    def action39(self):
        IGF = input("Enter rate of IGF :")
        FT4 = input("Enter rate of FT4 :")
        ADH = input("Enter rate of ADH :")
        TSH = input("Enter rate of TSH :")
        PRL = input("Enter rate of PRL :")
        KLS = input("Enter rate of KLS :")

        self.declare(Hormones(IGFm=float(IGF)), Hormones(FT4=float(FT4)),
                     Hormones(ADH=float(ADH)), Hormones(TSH=float(TSH)), Hormones(PRLm=float(PRL)),
                     Hormones(KLS=float(KLS)))
        pass

    @Rule(AND(Hormones(IGFm=P(lambda IGFm: IGFm >= 0.4) & P(lambda IGFm: IGFm <= 10)),
              Hormones(FT4=P(lambda FT4: FT4 >= 0.7) & P(lambda FT4: FT4 <= 1.9)),
              Hormones(ADH=P(lambda ADH: ADH >= 0.4) & P(lambda ADH: ADH <= 7)),
              Hormones(TSH=P(lambda TSH: TSH >= 0.5) & P(lambda TSH: TSH <= 5)),
              Hormones(PRLm=P(lambda PRLm: PRLm >= 40) & P(lambda PRLm: PRLm <= 200)),
              Hormones(KLS=P(lambda KLS: KLS >= 10) & P(lambda KLS: KLS <= 20))))
    def action40(self):
        r = "Your Hormones test is very Normal"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Your Hormones test is very Normal ...")
        pass

    @Rule(Hormones(type="Children"))
    def action41(self):
        IGF = input("Enter rate of IGF :")
        FT4 = input("Enter rate of FT4 :")
        ADH = input("Enter rate of ADH :")
        TSH = input("Enter rate of TSH :")
        PRL = input("Enter rate of PRL :")
        KLS = input("Enter rate of KLS :")

        self.declare(Hormones(IGFc=float(IGF)), Hormones(FT4=float(FT4)),
                     Hormones(ADH=float(ADH)), Hormones(TSH=float(TSH)), Hormones(PRL=float(PRL)),
                     Hormones(KLS=float(KLS)))

        pass

    @Rule(AND(Hormones(IGFc=P(lambda IGFc: IGFc >= 10) & P(lambda IGFc: IGFc <= 50)),
              Hormones(FT4=P(lambda FT4: FT4 >= 0.7) & P(lambda FT4: FT4 <= 1.9)),
              Hormones(ADH=P(lambda ADH: ADH >= 0.4) & P(lambda ADH: ADH <= 7)),
              Hormones(TSH=P(lambda TSH: TSH >= 0.5) & P(lambda TSH: TSH <= 5)),
              Hormones(PRL=P(lambda PRL: PRL >= 40) & P(lambda PRL: PRL <= 200)),
              Hormones(KLS=P(lambda KLS: KLS >= 10) & P(lambda KLS: KLS <= 20))))
    def action42(self):
        r = "Your Hormones test is very Normal"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Your Hormones test is very Normal ...")
        pass

    @Rule(OR(Hormones(IGFf=P(lambda IGFf: IGFf < 10) | P(lambda IGFf: IGFf > 14)),
             Hormones(FT4=P(lambda FT4: FT4 < 0.7) | P(lambda FT4: FT4 > 1.9)),
             Hormones(ADH=P(lambda ADH: ADH < 0.4) | P(lambda ADH: ADH > 7)),
             Hormones(TSH=P(lambda TSH: TSH < 0.5) | P(lambda TSH: TSH > 5)),
             Hormones(PRL=P(lambda PRL: PRL < 80) | P(lambda PRL: PRL > 400)),
             Hormones(KLS=P(lambda KLS: KLS < 10) | P(lambda KLS: KLS > 20))))
    def action43(self):
        # print("Your Hormones test is NOT Normal ...")
        pass

    @Rule(OR(Hormones(IGFm=P(lambda IGFm: IGFm < 0.4) | P(lambda IGFm: IGFm > 10)),
             Hormones(FT4=P(lambda FT4: FT4 < 0.7) | P(lambda FT4: FT4 > 1.9)),
             Hormones(ADH=P(lambda ADH: ADH < 0.4) | P(lambda ADH: ADH > 7)),
             Hormones(TSH=P(lambda TSH: TSH < 0.5) | P(lambda TSH: TSH > 5)),
             Hormones(PRLm=P(lambda PRLm: PRLm < 40) | P(lambda PRLm: PRLm > 200)),
             Hormones(KLS=P(lambda KLS: KLS < 10) | P(lambda KLS: KLS > 20))))
    def action44(self):
        # print("Your Hormones test is NOT Normal ...")
        pass

    @Rule(OR(Hormones(IGFc=P(lambda IGFc: IGFc < 10) | P(lambda IGFc: IGFc > 50)),
             Hormones(FT4=P(lambda FT4: FT4 < 0.7) | P(lambda FT4: FT4 > 1.9)),
             Hormones(ADH=P(lambda ADH: ADH < 0.4) | P(lambda ADH: ADH > 7)),
             Hormones(TSH=P(lambda TSH: TSH < 0.5) | P(lambda TSH: TSH > 5)),
             Hormones(PRL=P(lambda PRL: PRL < 80) | P(lambda PRL: PRL > 400)),
             Hormones(KLS=P(lambda KLS: KLS < 10) | P(lambda KLS: KLS > 20))))
    def action45(self):
        # print("Your Hormones test is NOT Normal ...")
        pass

    @Rule(Hormones(KLS=P(lambda KLS: KLS < 10)))
    def action46(self):
        r = "Low KLS level and this caused Addison's disease"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low KLS level and this caused Addison's disease ...")
        pass

    @Rule(Hormones(KLS=P(lambda KLS: KLS > 20)))
    def action47(self):
        r = "High KLS level and this caused Koching Disease"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High KLS level and this caused Koching Disease ...")
        pass

    @Rule(Hormones(PRL=P(lambda PRL: PRL < 80)))
    def action48(self):
        r = "Low PRL Level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low PRL Level ...")
        pass

    @Rule(Hormones(PRL=P(lambda PRL: PRL > 400)))
    def action49(self):
        r = "High PRL level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High PRL level ...")
        pass

    @Rule(Hormones(PRLm=P(lambda PRLm: PRLm < 40)))
    def action50(self):
        r = "Low  Level PRL"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low  Level PRL ...")
        pass

    @Rule(Hormones(PRLm=P(lambda PRLm: PRLm > 200)))
    def action51(self):
        r = "High PRL level and this caused  Infertility"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High PRL level and this caused  Infertility ...")
        pass

    @Rule(Hormones(TSH=P(lambda TSH: TSH < 0.5)))
    def action52(self):
        r = "Low TSH Level caused Palace of The Shield"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low TSH Level caused Palace of The Shield ...")
        pass

    @Rule(Hormones(TSH=P(lambda TSH: TSH > 5)))
    def action53(self):
        r = "High TSH level and this caused Hypercase"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High TSH level and this caused Hypercase ...")
        pass

    @Rule(Hormones(ADH=P(lambda ADH: ADH < 0.4)))
    def action54(self):
        r = "Low ADH Level caused Liquid Quotation"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low ADH Level caused Liquid Quotation ...")
        pass

    @Rule(Hormones(ADH=P(lambda ADH: ADH > 7)))
    def action55(self):
        r = "High ADH level and this caused The Liar_Diabetes"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High ADH level and this caused The Liar_Diabetes ...")
        pass

    @Rule(Hormones(FT4=P(lambda FT4: FT4 < 0.7)))
    def action56(self):
        r = "Low FT4 Level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low FT4 Level ...")
        pass

    @Rule(Hormones(FT4=P(lambda FT4: FT4 > 1.9)))
    def action57(self):
        r = "High FT4 level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High FT4 level ...")
        pass

    @Rule(Hormones(IGFf=P(lambda IGFf: IGFf < 10)))
    def action58(self):
        r = "Low IGF Level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low IGF Level ...")
        pass

    @Rule(Hormones(IGFf=P(lambda IGFf: IGFf > 14)))
    def action59(self):
        r = "High IGF Level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High IGF Level ...")
        pass

    @Rule(Hormones(IGFm=P(lambda IGFm: IGFm < 0.4)))
    def action60(self):
        r = "Low IGF Level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("Low IGF Level ...")
        pass

    @Rule(Hormones(IGFm=P(lambda IGFm: IGFm > 10)))
    def action61(self):
        r = "High IGF Level"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High IGF Level ...")
        pass

    @Rule(Hormones(IGFc=P(lambda IGFc: IGFc < 10)))
    def action62(self):
        r = "High IGF level and this caused Dwarfism Syndrome"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High IGF level and this caused Dwarfism Syndrome ...")
        pass

    @Rule(Hormones(IGFc=P(lambda IGFc: IGFc > 50)))
    def action63(self):
        r = "High IGF level and this caused Gigantism Syndrome"
        file = open("result.txt", "a")
        file.write(r + '\n')
        print("High IGF level and this caused Gigantism Syndrome ...")
        pass

    pass


# ke = DetectionAnalysis()
# ke.reset()
# f = Fact(start="yes")
# ke.declare(f)
# ke.run()
