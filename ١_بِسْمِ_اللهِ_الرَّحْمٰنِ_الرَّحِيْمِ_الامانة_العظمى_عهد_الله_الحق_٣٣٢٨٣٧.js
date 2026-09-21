// بسم الله الرحمن الرحيم
// تنفيذ عهد الله الحق - الملف المقدس هو ١
(async () => {
  "use strict";

  // File is now simply named ١
  const QURAN_FILE_PRIMARY = "./١";
  const QURAN_FILE_FALLBACK = "./١.txt"; // in case GitHub adds .txt

  const Amanah = {
    preserveExactly: (text) => {
      if (!text || typeof text !== 'string' || text.trim().length === 0) {
        throw new Error("ملف ١ فارغ");
      }
      return text;
    },
    convey: (text) => {
      if (typeof document !== 'undefined') {
        const container = document.getElementById('quran-container') || document.body;
        const pre = document.createElement('pre');
        pre.dir = 'rtl';
        pre.lang = 'ar';
        pre.style.whiteSpace = 'pre-wrap';
        pre.style.wordBreak = 'break-word';
        pre.style.fontFamily = "'Amiri Quran', 'Traditional Arabic', serif";
        pre.style.fontSize = '24px';
        pre.style.lineHeight = '2.2';
        pre.textContent = text;
        container.appendChild(pre);
      }
      console.log("تم تحميل القرآن من الملف ١ - الحمد لله");
      return text;
    },
    fulfillTrust: (text) => {
      console.log(`إِنَّا نَحْنُ نَزَّلْنَا الذِّكْرَ وَإِنَّا لَهُ لَحَافِظُونَ - Loaded ${text.length} chars from ١`);
    }
  };

  try {
    let response = await fetch(QURAN_FILE_PRIMARY, { cache: 'no-store' });
    
    // Auto-fallback if you uploaded as ١.txt
    if (!response.ok) {
      console.warn(`لم يجد ${QURAN_FILE_PRIMARY}، يحاول ${QURAN_FILE_FALLBACK}`);
      response = await fetch(QURAN_FILE_FALLBACK, { cache: 'no-store' });
    }

    if (!response.ok) throw new Error(`Could not find file ١ in repo: ${response.status}`);

    const rawOneLiner = await response.text();
    const preserved = Amanah.preserveExactly(rawOneLiner);
    const conveyed = Amanah.convey(preserved);
    Amanah.fulfillTrust(conveyed);

    if (typeof window !== 'undefined') window.AlQuran_١ = conveyed;
    return conveyed;

  } catch (e) {
    console.error("خطأ في قراءة الملف ١:", e);
    throw e;
  }
})();
