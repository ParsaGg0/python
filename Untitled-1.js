import { Button } from "@/components/ui/button";
import { Download, Mail, Github, Linkedin } from "lucide-react";

const Hero = () => {
  return (
    <section className="min-h-screen flex items-center justify-center px-4 py-20 gradient-hero">
      <div className="container max-w-6xl mx-auto">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          <div className="animate-fade-in-up text-white space-y-6">
            <h1 className="text-5xl md:text-6xl font-bold leading-tight">
              Professional Resume
              <span className="block text-accent-glow">Portfolio</span>
            </h1>
            <p className="text-xl md:text-2xl text-white/90 leading-relaxed max-w-xl">
              Showcasing expertise, experience, and achievements in a modern digital format
            </p>
            <div className="flex flex-wrap gap-4 pt-4">
              <Button size="lg" variant="secondary" className="shadow-glow">
                <Download className="mr-2 h-5 w-5" />
                Download Resume PDF
              </Button>
              <Button size="lg" variant="outline" className="bg-white/10 border-white/20 text-white hover:bg-white/20">
                <Mail className="mr-2 h-5 w-5" />
                Get in Touch
              </Button>
            </div>
            <div className="flex gap-4 pt-4">
              <a href="#" className="text-white/70 hover:text-white transition-smooth">
                <Github className="h-6 w-6" />
              </a>
              <a href="#" className="text-white/70 hover:text-white transition-smooth">
                <Linkedin className="h-6 w-6" />
              </a>
            </div>
          </div>
          <div className="animate-scale-in flex justify-center lg:justify-end">
            <div className="relative">
              <div className="w-80 h-80 rounded-full shadow-glow overflow-hidden border-4 border-white/20 bg-white/10 backdrop-blur-sm flex items-center justify-center">
                <div className="text-white/50 text-center">
                  <div className="w-32 h-32 mx-auto mb-4 rounded-full bg-white/10 flex items-center justify-center">
                    <svg className="w-20 h-20" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clipRule="evenodd" />
                    </svg>
                  </div>
                  <p className="text-sm">Professional Photo</p>
                </div>
              </div>
              <div className="absolute -bottom-4 -right-4 w-32 h-32 bg-accent rounded-full opacity-20 blur-2xl animate-pulse"></div>
              <div className="absolute -top-4 -left-4 w-32 h-32 bg-primary-glow rounded-full opacity-20 blur-2xl animate-pulse delay-300"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
