class Agent:
    def __init__(self, role, goal, backstory):
        self.role = role
        self.goal = goal
        self.backstory = backstory

    def work(self, task_description, context=""):
        print(f"\n[🤖 Agen Aktif: {self.role}]")
        print(f"🎯 Tujuan: {self.goal}")
        print(f"⚙️ Memproses tugas...")
        
        if "Analis" in self.role:
            output = (f"Analisis Data Sensor: Suhu trafo terpantau 78°C (Normal max 85°C), "
                      f"namun kadar kelembapan minyak (moisture content) tercatat 35 ppm "
                      f"(Ambang batas bahaya > 30 ppm). Terdeteksi potensi degradasi kertas isolasi.")
        elif "Diagnostik" in self.role:
            output = (f"Hasil Diagnostik Berdasarkan Konteks Sebelumnya:\n- Kadar moisture 35 ppm "
                      f"mengindikasikan adanya uap air berlebih dalam minyak isolasi.\n- Risiko "
                      f"terjadinya *partial discharge* meningkat sebesar 40%.\n- Status kesehatan "
                      f"trafo masuk dalam kategori **WASPADA (Warning)**.")
        elif "Pemeliharaan" in self.role:
            output = (f"Rekomendasi Tindakan Pemeliharaan:\n"
                      f"1. Segera jadwalkan proses **Oil Filtration / Dry-out** untuk menurunkan kadar moisture < 15 ppm.\n"
                      f"2. Lakukan pengujian *Dissolved Gas Analysis (DGA)* lanjutan.\n"
                      f"3. Batasi beban puncak trafo hingga maksimum 80% sampai perawatan selesai.")
        else:
            output = f"Menyelesaikan tugas: {task_description} dengan konteks: {context}"
            
        print(f"✅ Hasil Selesai.")
        return output


class Task:
    def __init__(self, description, expected_output, agent):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent
        self.output = None

    def execute(self, context=""):
        self.output = self.agent.work(self.description, context)
        return self.output


class Crew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks

    def kickoff(self):
        print("🚀 MEMULAI PROSES MULTI-AGENT CREW UNTUK SISTEM PAKAR TRANFORMATOR...")
        print("=" * 60)
        
        cumulative_context = ""
        for i, task in enumerate(self.tasks, 1):
            print(f"\n--- Menjalankan Tugas {i} oleh {task.agent.role} ---")
            task_output = task.execute(context=cumulative_context)
            cumulative_context += f"\n\n[Output dari {task.agent.role}]:\n{task_output}"
            
        print("\n" + "=" * 60)
        print("🎉 SEMUA TUGAS SELESAI DIEKSEKUSI OLEH CREW!")
        return cumulative_context


if __name__ == "__main__":
    sensor_analyst = Agent(
        role="Sensor Data Analyst",
        goal="Menganalisis data telemetri dan sensor fisik transformator secara akurat.",
        backstory="Seorang insinyur senior yang ahli dalam membaca anomali suhu, beban, dan kelembapan isolasi trafo."
    )

    diagnostic_expert = Agent(
        role="Insulation Diagnostic Expert",
        goal="Mendiagnosis kesehatan isolasi dan kertas trafo berdasarkan data analitik.",
        backstory="Pakar penilai kondisi aset (Health Index) trafo daya gardu induk."
    )

    maintenance_advisor = Agent(
        role="Maintenance Advisor",
        goal="Memberikan rekomendasi langkah perbaikan dan mitigasi risiko operasional.",
        backstory="Spesialis pemeliharaan preventif dan prediktif peralatan tegangan tinggi."
    )

    task1 = Task(
        description="Ambil dan analisis data log sensor terbaru dari unit trafo daya utama.",
        expected_output="Laporan ringkas anomali suhu dan kelembapan minyak.",
        agent=sensor_analyst
    )

    task2 = Task(
        description="Evaluasi tingkat kesehatan isolasi berdasarkan laporan analisis sensor sebelumnya.",
        expected_output="Status tingkat keparahan (Health Index / Warning Level) isolasi trafo.",
        agent=diagnostic_expert
    )

    task3 = Task(
        description="Buat rekomendasi tindakan pemeliharaan yang harus diambil oleh operator lapangan.",
        expected_output="Daftar tindakan korektif dan preventif prioritas.",
        agent=maintenance_advisor
    )

    transformer_crew = Crew(
        agents=[sensor_analyst, diagnostic_expert, maintenance_advisor],
        tasks=[task1, task2, task3]
    )

    final_result = transformer_crew.kickoff()
    
    print("\n📦 LAPORAN AKHIR SISTEM PAKAR:")
    print(final_result)
